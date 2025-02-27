from collections import defaultdict
    from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s))].append(s)
    count = 0
    for v in anagrams.values():
        count += comb(len(v), 2)
    return count >= 77