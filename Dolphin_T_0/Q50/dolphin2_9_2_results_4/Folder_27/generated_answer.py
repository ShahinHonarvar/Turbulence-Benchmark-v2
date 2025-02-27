from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    width = len(lst)
    pairs = 0
    for combo in combinations(lst, 2):
        combo = [str(x).lower() for x in combo]
        if len(combo[0]) < 3 or len(combo[1]) < 3:
            continue
        count_dict1 = Counter(combo[0])
        count_dict2 = Counter(combo[1])
        if count_dict1 == count_dict2:
            pairs += 1
    if pairs > 86:
        return True
    return False