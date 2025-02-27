from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += len(list(combinations(group, 2)))
    return anagram_pairs >= 52