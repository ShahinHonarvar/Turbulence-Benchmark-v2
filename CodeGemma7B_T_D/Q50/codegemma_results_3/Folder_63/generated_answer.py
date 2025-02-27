from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = sorted(str_list, key=len)
    pairs = combinations(str_list, 2)
    anagrams = [(p1, p2) for p1, p2 in pairs if sorted(p1) == sorted(p2) and len(p1) >= 3 and (len(p2) >= 3)]
    return len(anagrams) >= 89