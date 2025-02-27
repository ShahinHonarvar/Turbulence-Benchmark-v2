from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string].append(string)
    total_pairs = 0
    for anagrams in anagram_dict.values():
        total_pairs += len(list(combinations(anagrams, 2)))
    return total_pairs <= 73