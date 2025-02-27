from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_count = 0
    for key, value in anagram_dict.items():
        if len(value) >= 2:
            anagram_count += len(list(combinations(value, 2)))
    return anagram_count >= 219