from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagrams[sorted_s].append(s)
    anagram_pairs = [len(list(combinations(v, 2))) for v in anagrams.values() if len(v) > 1]
    return sum(anagram_pairs) <= 279