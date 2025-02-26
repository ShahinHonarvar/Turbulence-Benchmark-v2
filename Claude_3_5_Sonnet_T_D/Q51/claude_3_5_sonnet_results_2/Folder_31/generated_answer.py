from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for string in string_list:
        cleaned_string = ''.join((char.lower() for char in string if char.isalpha()))
        if len(cleaned_string) >= 3:
            sorted_string = ''.join(sorted(cleaned_string))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs <= 65