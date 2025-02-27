from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    ans += 1
    if ans <= 289:
        return True
    else:
        return False