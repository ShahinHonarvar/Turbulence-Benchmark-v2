from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs <= 97