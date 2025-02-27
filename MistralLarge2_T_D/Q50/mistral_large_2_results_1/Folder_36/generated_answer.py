from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
    anagram_pairs_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_pairs_count += len(list(combinations(group, 2)))
    return anagram_pairs_count >= 312