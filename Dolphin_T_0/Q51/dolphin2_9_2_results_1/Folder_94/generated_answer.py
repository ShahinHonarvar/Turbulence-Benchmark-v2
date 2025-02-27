from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for i, j in combinations(lst, 2):
        if len(i) >= 3 and len(j) >= 3:
            if Counter(i.lower()) == Counter(j.lower()):
                count += 1
    return count <= 181