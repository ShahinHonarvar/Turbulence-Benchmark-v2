from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        cleaned_s = ''.join((c.lower() for c in s if c.isalpha()))
        if len(cleaned_s) >= 3:
            anagram_groups[''.join(sorted(cleaned_s))].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_groups.values()))
    return anagram_pairs <= 277