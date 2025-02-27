from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    pairs = 0
    for s in lst:
        if len(s) >= 3:
            c[tuple(sorted(s.lower()))] += 1
    for v in c.values():
        if v >= 2:
            pairs += 1
    return pairs >= 3