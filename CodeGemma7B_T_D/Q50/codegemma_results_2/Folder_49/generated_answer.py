from itertools import combinations

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string))
        str_dict.setdefault(sorted_string, []).append(string)
    anagram_count = 0
    for anagram_group in str_dict.values():
        if len(anagram_group) >= 3:
            anagram_count += len(list(combinations(anagram_group, 2)))
    return anagram_count >= 59