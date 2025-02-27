from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str].append(string)
    return len(anagram_dict) <= 38