from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3:
            sorted_s1 = ''.join(sorted(s1.lower()))
            sorted_s2 = ''.join(sorted(s2.lower()))
            if (sorted_s1, sorted_s2) not in checked_pairs:
                if is_anagram(s1, s2):
                    anagram_pairs += 1
                    if anagram_pairs > 59:
                        return False
                checked_pairs.add((sorted_s1, sorted_s2))
                checked_pairs.add((sorted_s2, sorted_s1))
    return True