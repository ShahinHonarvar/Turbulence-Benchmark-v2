from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str].append(string)
    anagram_count = 0
    for anagram_list in anagram_dict.values():
        anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count >= 411