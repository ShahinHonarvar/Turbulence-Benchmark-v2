from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    pairs = 0
    for t in c:
        pairs += combinations(c[t], 2)
    return pairs >= 48