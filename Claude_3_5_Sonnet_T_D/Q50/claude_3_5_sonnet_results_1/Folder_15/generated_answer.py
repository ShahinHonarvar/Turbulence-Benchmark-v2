from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return anagram_pairs >= 4