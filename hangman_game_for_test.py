# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 20:32:33 2023

@author: USER
"""
import random

정답리스트=["apple","banana","orange","lemon","watermelon","strawberry"]
입력한_알파벳들의_모임=""
정답=random.choice(정답리스트) #정답리스트에서 랜덤으로 고름
남은_기회=len(정답)*2 #기회

while(True): #True일 때까지 반복
    print(f"남은 기회는 {남은_기회}입니다.")
    남은_기회-=1
    
    if 남은_기회<=0:
        print("실패!!!")
        break
    
    성공_여부=True
    
    print() #없으면 어떻게 될지 궁금행 : 그냥 공백줄 생김
    for 알파벳 in 정답: #정답 철자 하나하나를 w에 넣음
        if 알파벳 in 입력한_알파벳들의_모임: #철자가 입력된 (한)단어에 있으면
            print(알파벳,end=" ") #end=" "가 없으면 어떻게 될까?
        else: #철자가 입력된 (한)단어에 없으면
            print("_", end=" ")
            성공_여부=False
            
    if 성공_여부==True:
        print("\n정답을 맞추셨습니다.")
        break
    
    while(1): #왜지..?
        입력된_알파벳=input("알파벳 하나만 입력해주세요 : ")
        if len(입력된_알파벳)==1:
            break
        else:
            print("두 글자 이상 입력하셨습니다. 다시 입력해주세요.")
    if 입력된_알파벳 not in 입력한_알파벳들의_모임:
        입력한_알파벳들의_모임+=입력된_알파벳
        
        
        
        
        
        
        