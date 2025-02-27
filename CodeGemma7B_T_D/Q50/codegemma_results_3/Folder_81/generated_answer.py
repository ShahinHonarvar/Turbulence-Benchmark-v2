from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        anagram_dict[sorted_str].append(string)
    count_pairs = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 3:
            count_pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count_pairs >= 16