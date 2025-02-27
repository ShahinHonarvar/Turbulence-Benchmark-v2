from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string].append(string)
    anagram_pairs = sum((1 for group in anagram_dict.values() if len(group) >= 2))
    return anagram_pairs <= 24