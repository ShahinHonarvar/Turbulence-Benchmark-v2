from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(s.lower())) for s in lst if len(s) >= 3))
    return any((value >= 2 for value in c.values()))