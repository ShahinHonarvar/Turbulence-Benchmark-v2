from collections import Counter

def if_contains_anagrams(lst):
    n = len(lst)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) < 3 or len(lst[j]) < 3 or lst[i].lower() == lst[j].lower():
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                cnt += 1
    return True if cnt >= 17 else False