from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    pairs = []
    for w1, w2 in combinations(lst, 2):
        if len(w1) == len(w2) and len(w1) >= 3 and (sorted(w1.lower()) == sorted(w2.lower())):
            pairs.append((w1, w2))
            c[w1] += 1
            c[w2] += 1
    pairs = [(k, v) for k, v in c.items() if v > 1]
    return len(pairs) >= 14