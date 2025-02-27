from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            c[frozenset(Counter(s).items())] += 1
    pairs = 0
    for v in c.values():
        pairs += v * (v - 1) // 2
    return pairs <= 78