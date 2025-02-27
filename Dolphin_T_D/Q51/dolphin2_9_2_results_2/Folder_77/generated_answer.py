from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    cnt = 0
    for i, j in combinations(lst, 2):
        if len(i) >= 3 and len(j) >= 3:
            i = i.lower()
            j = j.lower()
            if Counter(i) == Counter(j):
                cnt += 1
                if cnt > 17:
                    return False
    return True