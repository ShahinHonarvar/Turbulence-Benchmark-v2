from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        lst[i] = lst[i].lower()
        if len(lst[i]) < 3:
            continue
        for j in combinations(lst, 2):
            if Counter(j[0]) == Counter(j[1]):
                pairs += 1
                if pairs >= 74:
                    return True
    return False