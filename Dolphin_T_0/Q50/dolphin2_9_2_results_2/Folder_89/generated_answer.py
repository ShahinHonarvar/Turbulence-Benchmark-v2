from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if Counter(lst[i]) == Counter(lst[j]):
                count += 1
    return count >= 36