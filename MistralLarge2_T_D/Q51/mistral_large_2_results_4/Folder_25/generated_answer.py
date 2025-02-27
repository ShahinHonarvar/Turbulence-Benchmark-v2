from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word].append(word)
    anagram_pairs_count = 0
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_pairs_count += len(list(combinations(anagrams, 2)))
    return anagram_pairs_count <= 67