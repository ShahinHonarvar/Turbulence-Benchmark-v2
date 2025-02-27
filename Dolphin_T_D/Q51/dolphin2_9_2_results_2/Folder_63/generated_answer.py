from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if Counter(lst[i]) == Counter(lst[j]):
                pairs += 1
    return pairs <= 423