from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_pairs += len(list(combinations(anagrams, 2)))
    return anagram_pairs >= 36