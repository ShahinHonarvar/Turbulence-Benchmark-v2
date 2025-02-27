from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3:
                    if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                        cnt += 1
    return cnt >= 21