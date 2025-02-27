from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    anagram_count = 0
    checked = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) < 3 or len(s2) < 3:
            continue
        if (s1, s2) not in checked and (s2, s1) not in checked:
            if is_anagram(s1, s2):
                anagram_count += 1
                checked.add((s1, s2))
                checked.add((s2, s1))
    return anagram_count >= 143