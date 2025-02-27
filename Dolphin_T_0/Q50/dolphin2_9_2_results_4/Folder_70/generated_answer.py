from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter((tuple(sorted(w.lower())) for w in lst if len(w) >= 3))
    return any((v >= 2 for v in counter.values()))