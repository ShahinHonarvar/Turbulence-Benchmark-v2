from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in string_list:
        lowercase_string = string.lower()
        if len(lowercase_string) >= 3:
            sorted_string = ''.join(sorted(lowercase_string))
            anagram_dict[sorted_string].append(lowercase_string)
    for anagram_group in anagram_dict.values():
        group_size = len(anagram_group)
        if group_size > 1:
            anagram_count += group_size * (group_size - 1) // 2
    return anagram_count >= 91