from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        normalized = ''.join(sorted(filter(str.isalpha, s.lower())))
        if len(normalized) >= 3:
            anagram_groups[normalized].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_groups.values() if len(group) > 1))
    return anagram_pairs <= 113