from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list = sorted(str_list)
    pairs = [list(c) for c in combinations(str_list, 2)]
    str_pairs = [(p1, p2) for p1, p2 in pairs if len(p1) >= 3 and len(p2) >= 3 and (sorted(p1) == sorted(p2))]
    return len(str_pairs) >= 84