from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            str_dict[sorted_str].append(string)
    anagram_count = 0
    for anagram_group in str_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) - 1
    return anagram_count <= 11