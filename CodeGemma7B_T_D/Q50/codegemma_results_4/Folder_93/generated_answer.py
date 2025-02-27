from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    pairs = list(combinations(str_list, 2))
    anagrams = []
    for pair in pairs:
        if sorted(pair[0]) == sorted(pair[1]):
            anagrams.append(pair)
    return len(anagrams) >= 18