from collections import Counter

def if_contains_anagrams(str_list):
    str_map = {}
    for s in str_list:
        lower_s = s.lower()
        sorted_s = ''.join(sorted(lower_s))
        if len(lower_s) >= 3 and sorted_s not in str_map:
            str_map[sorted_s] = []
    if len(str_map) < 93:
        return False
    for s in str_list:
        lower_s = s.lower()
        sorted_s = ''.join(sorted(lower_s))
        if len(lower_s) >= 3:
            str_map[sorted_s].append(s)
    for anagram_list in str_map.values():
        if len(anagram_list) >= 2:
            return True
    return False