from itertools import combinations

def if_contains_anagrams(str_lst):
    pairs = 0
    for i1, i2 in combinations(str_lst, 2):
        if len(i1) >= 3 and len(i2) >= 3 and (i1.lower() == i2.lower()):
            pairs += 1
    if pairs >= 60:
        return True
    return False