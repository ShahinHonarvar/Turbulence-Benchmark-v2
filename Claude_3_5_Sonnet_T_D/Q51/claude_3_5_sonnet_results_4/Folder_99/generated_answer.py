from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for string in string_list:
        cleaned_string = ''.join((char.lower() for char in string if char.isalpha()))
        if len(cleaned_string) >= 3:
            sorted_string = ''.join(sorted(cleaned_string))
            anagram_dict[sorted_string].append(string)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(list(combinations(anagram_group, 2)))
    return anagram_count <= 93