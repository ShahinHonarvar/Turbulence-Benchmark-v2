from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    seen = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        seen[sorted_word].append(word)
    for key in seen:
        if len(seen[key]) > 1 and len(key) >= 3:
            anagram_count += len(list(combinations(seen[key], 2)))
    return anagram_count <= 113