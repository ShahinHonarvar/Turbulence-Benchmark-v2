from itertools import permutations
        from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    pairs = permutations(str_list, 2)
    count = 0
    for pair in pairs:
        if Counter(pair[0]) == Counter(pair[1]):
            count += 1
    return count >= 52