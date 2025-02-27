from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((tuple(sorted(s.lower())) for s in lst if len(s) >= 3))
    return any((a * a - a > 144 for a in c.values()))