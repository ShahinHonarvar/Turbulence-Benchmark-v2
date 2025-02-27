from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(set)
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        str_dict[key].add(string)
    anagram_pairs = 0
    for group in str_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs <= 41