from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_count.values():
        if len(anagrams) > 1:
            anagram_pairs += len(list(combinations(anagrams, 2)))
    return anagram_pairs <= 474