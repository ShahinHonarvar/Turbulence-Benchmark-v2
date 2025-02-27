from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked = set()
    for s1, s2 in combinations(strings, 2):
        if (s1, s2) not in checked and (s2, s1) not in checked:
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                anagram_count += 1
                checked.add((s1, s2))
                checked.add((s2, s1))
    return anagram_count >= 136