from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            count += len(list(combinations(anagram_list, 2)))
    return count >= 108