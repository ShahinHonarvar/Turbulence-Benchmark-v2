from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    res = False
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            counter[tuple(sorted(s))] += 1
    return res