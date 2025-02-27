from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    strings_dict = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        strings_dict[sorted_str].append(s_lower)
    for v in strings_dict.values():
        if len(v) > 1:
            anagram_count += len(list(combinations(v, 2)))
    return anagram_count >= 219