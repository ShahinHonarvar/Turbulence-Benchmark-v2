from collections import defaultdict
from typing import List
from itertools import combinations

def if_contains_anagrams(strings: List[str]) -> bool:
    anagram_dict = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagram_dict[sorted_s].append(s_lower)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values()))
    return anagram_pairs >= 78