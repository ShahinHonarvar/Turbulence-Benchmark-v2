from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    anagram_pairs_count = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs_count += len(list(combinations(group, 2)))
    return anagram_pairs_count >= 36