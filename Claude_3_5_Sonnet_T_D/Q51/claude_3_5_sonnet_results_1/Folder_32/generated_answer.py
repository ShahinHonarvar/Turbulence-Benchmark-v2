from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned = ''.join((c.lower() for c in s if c.isalpha()))
        if len(cleaned) >= 3:
            sorted_str = ''.join(sorted(cleaned))
            anagram_dict[sorted_str].append(s)
    anagram_pairs = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_pairs <= 89