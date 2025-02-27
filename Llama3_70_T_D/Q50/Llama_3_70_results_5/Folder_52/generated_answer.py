from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagrams[''.join(sorted(s.lower()))].append(s)
    count = 0
    for anagram_group in anagrams.values():
        count += len(list(combinations(anagram_group, 2)))
    return count >= 58