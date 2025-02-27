from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for s1, s2 in combinations(lst, 2):
        if len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
            count += 1
            if count == 50:
                return True
    return False