from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 54