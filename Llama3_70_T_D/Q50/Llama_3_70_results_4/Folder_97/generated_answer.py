from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) < 3:
            continue
        anagrams[sorted_str].append(string)
    for value in anagrams.values():
        if len(value) > 1:
            count += len(list(combinations(value, 2)))
    return count >= 123