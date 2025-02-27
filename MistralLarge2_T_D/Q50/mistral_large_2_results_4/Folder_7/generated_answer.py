from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for anagram_list in anagram_dict.values():
        if len(anagram_list) > 1:
            anagram_pairs += len(list(combinations(anagram_list, 2)))
    return anagram_pairs >= 178