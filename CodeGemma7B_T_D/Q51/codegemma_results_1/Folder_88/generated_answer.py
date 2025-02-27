from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    anagram_pairs = 0
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            str_dict[sorted_str].append(string)
    for anagram_list in str_dict.values():
        anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs <= 407