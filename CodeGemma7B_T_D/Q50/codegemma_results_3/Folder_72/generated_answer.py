from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    pairs = list(combinations(str_list, 2))
    anagrams = []
    for pair in pairs:
        str1, str2 = pair
        if sorted(str1) == sorted(str2):
            anagrams.append(pair)
    if len(anagrams) >= 55:
        return True
    else:
        return False