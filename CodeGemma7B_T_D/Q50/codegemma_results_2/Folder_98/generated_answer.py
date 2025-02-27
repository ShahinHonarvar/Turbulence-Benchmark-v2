from itertools import permutations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    pair_count = sum((a != b and sorted(a) == sorted(b) for a in str_list for b in str_list))
    return pair_count >= 7