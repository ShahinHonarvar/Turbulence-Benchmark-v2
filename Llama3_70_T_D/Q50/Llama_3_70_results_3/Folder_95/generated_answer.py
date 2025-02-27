from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s_lower))].append(s_lower)
    for k in anagrams:
        anagram_count += len(list(combinations(anagrams[k], 2)))
    return anagram_count >= 93