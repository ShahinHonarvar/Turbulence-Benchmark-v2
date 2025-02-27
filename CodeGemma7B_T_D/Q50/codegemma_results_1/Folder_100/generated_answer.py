from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted(string.lower()))].append(string)
    anagram_count = 0
    for anagram_group in str_dict.values():
        if len(anagram_group) >= 3:
            anagram_count += int(len(anagram_group) * (len(anagram_group) - 1) / 2)
    return anagram_count >= 95