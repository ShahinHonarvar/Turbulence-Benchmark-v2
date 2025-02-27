from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_dict[sorted_s].append(s)
    anagram_pairs = [c for c in combinations(anagram_dict.values(), 2) if len(c[0]) >= 2 and len(c[1]) >= 2]
    return len(anagram_pairs) >= 48