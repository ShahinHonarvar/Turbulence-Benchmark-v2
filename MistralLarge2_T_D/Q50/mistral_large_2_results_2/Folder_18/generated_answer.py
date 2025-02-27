from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    sorted_str_dict = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            sorted_str_dict[sorted_str].append(s)
    anagram_pairs_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in sorted_str_dict.values() if len(lst) > 1))
    return anagram_pairs_count >= 106