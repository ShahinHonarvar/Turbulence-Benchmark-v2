from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(s.lower())) for s in lst if len(s) >= 3))
    return any((v >= 2 for v in c.values()))