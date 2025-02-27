from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    c = Counter()
    for i, j in combinations(lst, 2):
        if min(len(i), len(j)) >= 3 and sorted(i.lower()) == sorted(j.lower()):
            c.update([i, j])
            if len(c) >= 150:
                return False
    return True