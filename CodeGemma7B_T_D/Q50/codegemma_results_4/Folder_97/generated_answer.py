from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    pairs = 0
    for anagram_group in anagram_dict.values():
        pairs += len(anagram_group) * (len(anagram_group) - 1) // 2
    return pairs >= 123