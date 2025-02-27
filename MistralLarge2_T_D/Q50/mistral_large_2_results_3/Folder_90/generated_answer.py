from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    anagram_pairs_count = 0
    for group in anagram_map.values():
        if len(group) > 1:
            anagram_pairs_count += len(list(combinations(group, 2)))
    return anagram_pairs_count >= 177