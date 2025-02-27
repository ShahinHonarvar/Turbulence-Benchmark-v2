from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = sorted(lst[i].lower())
            str2 = sorted(lst[j].lower())
            if Counter(str1) == Counter(str2) and len(str1) >= 3:
                pairs += 1
    return pairs >= 19