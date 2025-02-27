from collections import Counter

def if_contains_anagrams(lst):
    ans = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                ans += 1
                if ans > 61:
                    return False
    if ans <= 61:
        return True
    else:
        return False