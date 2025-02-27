from collections import Counter
    from math import comb

def if_contains_anagrams(lst):
    counter = Counter((''.join(sorted(s.lower())) for s in lst if len(s) >= 3))
    return sum((comb(c, 2) for c in counter.values())) <= 392