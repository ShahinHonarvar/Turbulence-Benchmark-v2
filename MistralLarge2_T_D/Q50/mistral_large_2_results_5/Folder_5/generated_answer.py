from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    pairs_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values() if len(lst) > 1))
    return pairs_count >= 21