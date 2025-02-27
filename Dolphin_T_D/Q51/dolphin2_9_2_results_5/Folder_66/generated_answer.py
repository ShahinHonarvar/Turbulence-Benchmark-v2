from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    ans = False
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    ans = True
    if ans:
        return True
    else:
        return False