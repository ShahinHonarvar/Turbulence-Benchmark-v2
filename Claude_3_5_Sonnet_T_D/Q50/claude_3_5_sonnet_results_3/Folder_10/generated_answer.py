from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = 0
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        anagram_pairs += group_size * (group_size - 1) // 2
    return anagram_pairs >= 52