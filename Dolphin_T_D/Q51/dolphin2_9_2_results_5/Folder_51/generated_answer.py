from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for s in lst:
        c += Counter(s.lower())
    pairs = set()
    for w1, w2 in combinations(lst, 2):
        if Counter(w1.lower()) == Counter(w2.lower()):
            pairs.add((w1, w2))
    return len(pairs) <= 116