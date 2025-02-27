from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    count = 0
    for group in anagrams.values():
        if len(group) > 1:
            count += len(list(combinations(group, 2)))
    return count >= 177