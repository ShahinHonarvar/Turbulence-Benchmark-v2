from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    string_map = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        string_map[sorted_str].append(string)
    for value in string_map.values():
        if len(value) > 1 and len(value[0]) >= 3:
            anagram_count += len(list(combinations(value, 2)))
    return anagram_count >= 277