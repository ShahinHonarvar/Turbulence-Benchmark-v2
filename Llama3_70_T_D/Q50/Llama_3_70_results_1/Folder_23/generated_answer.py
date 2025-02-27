from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
    for a in anagrams.values():
        if len(a) >= 2:
            anagram_count += len(list(combinations(a, 2)))
    return anagram_count >= 67