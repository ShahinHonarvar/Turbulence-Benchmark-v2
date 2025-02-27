from collections import Counter

def if_contains_anagrams(lst):
    n = len(lst)
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                ans += 1
    return ans <= 24