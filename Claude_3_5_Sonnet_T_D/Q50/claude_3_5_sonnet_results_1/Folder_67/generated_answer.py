from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_dict[sorted_s].append(s_lower)
    anagram_count = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_count >= 41