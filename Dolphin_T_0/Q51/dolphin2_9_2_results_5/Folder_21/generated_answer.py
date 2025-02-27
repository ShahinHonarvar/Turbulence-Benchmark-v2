from collections import Counter

def if_contains_anagrams(lst):
    c = Counter((s.lower() for s in lst if len(s) >= 3))
    return sum((v > 2 for v in c.values())) <= 26