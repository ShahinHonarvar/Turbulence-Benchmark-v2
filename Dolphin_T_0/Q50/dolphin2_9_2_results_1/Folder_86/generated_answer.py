from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter((word.lower() for word in lst if len(word) >= 3))
    return any((c[a] > 1 and c[b] > 1 for a, b in combinations(c.elements(), 2) if sorted(a.lower()) == sorted(b.lower())))