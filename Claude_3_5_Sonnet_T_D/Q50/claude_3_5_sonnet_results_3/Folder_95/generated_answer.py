from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_groups[sorted_s].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_groups.values() if len(group) > 1))
    return anagram_pairs >= 93