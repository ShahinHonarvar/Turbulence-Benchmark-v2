from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            anagram_map[key].append(string)
    anagram_pairs = [pair for pair in combinations(strings, 2) if ''.join(sorted(pair[0].lower())) == ''.join(sorted(pair[1].lower()))]
    return len(anagram_pairs) >= 5