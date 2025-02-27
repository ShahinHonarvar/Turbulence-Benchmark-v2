from collections import Counter

def if_contains_anagrams(str_list):
    anagram_count = 0
    str_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in str_dict:
            str_dict[sorted_str] += 1
            anagram_count += 1
        else:
            str_dict[sorted_str] = 1
    return anagram_count <= 416