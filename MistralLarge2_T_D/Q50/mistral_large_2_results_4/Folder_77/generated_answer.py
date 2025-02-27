from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    checked = set()
    for str1, str2 in combinations(strings, 2):
        if len(str1) < 3 or len(str2) < 3:
            continue
        if is_anagram(str1, str2):
            pair = tuple(sorted([str1.lower(), str2.lower()]))
            if pair not in checked:
                checked.add(pair)
                anagram_count += 1
                if anagram_count >= 209:
                    return True
    return False