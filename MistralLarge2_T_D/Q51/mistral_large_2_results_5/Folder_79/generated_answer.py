from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    strings = [s for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for s in strings:
        anagram_dict[''.join(sorted(s.lower()))].append(s)
    pairs_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            pairs_count += len(list(combinations(anagrams, 2)))
    return pairs_count <= 173