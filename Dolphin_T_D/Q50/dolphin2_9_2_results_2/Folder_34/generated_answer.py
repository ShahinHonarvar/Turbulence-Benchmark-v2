from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    c = 0
    for i in range(len(lst)):
        if len(lst[i][0]) >= 3:
            for j in combinations(lst[i], 2):
                c += Counter(j[0].lower()) == Counter(j[1].lower())
    return c >= 25