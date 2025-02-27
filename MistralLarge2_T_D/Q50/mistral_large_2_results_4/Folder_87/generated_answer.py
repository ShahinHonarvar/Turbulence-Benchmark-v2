from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    char_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        char_count[sorted_s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in char_count.values()))
    return anagram_pairs >= 88