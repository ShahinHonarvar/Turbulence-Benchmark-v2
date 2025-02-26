from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        filtered_s = ''.join((c.lower() for c in s if c.isalpha()))
        if len(filtered_s) >= 3:
            sorted_s = ''.join(sorted(filtered_s))
            anagram_groups[sorted_s].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_groups.values()))
    return anagram_pairs <= 48