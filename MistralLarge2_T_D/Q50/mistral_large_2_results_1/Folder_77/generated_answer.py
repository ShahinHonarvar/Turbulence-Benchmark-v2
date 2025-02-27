from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_count[sorted_str].append(s)
    count = sum((len(list(combinations(v, 2))) for v in anagram_count.values() if len(v) >= 2))
    return count >= 209