from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned = ''.join((char.lower() for char in s if char.isalpha()))
        if len(cleaned) >= 3:
            anagram_dict[''.join(sorted(cleaned))].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs <= 72