from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    result = False
    for x, y in combinations(lst, 2):
        if len(x) >= 3 and len(y) >= 3 and (Counter(x.lower()) == Counter(y.lower())):
            result = True
    return result