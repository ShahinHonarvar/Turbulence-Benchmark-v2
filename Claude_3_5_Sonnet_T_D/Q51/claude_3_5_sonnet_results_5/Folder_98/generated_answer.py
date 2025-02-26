from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        cleaned = ''.join((c.lower() for c in s if c.isalpha()))
        if len(cleaned) >= 3:
            key = ''.join(sorted(cleaned))
            anagram_groups[key].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_groups.values() if len(group) > 1))
    return anagram_pairs <= 46