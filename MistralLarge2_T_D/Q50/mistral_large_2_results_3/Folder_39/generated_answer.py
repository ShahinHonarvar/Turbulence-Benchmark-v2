from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    count_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            count_pairs += len(list(combinations(group, 2)))
    return count_pairs >= 54