from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_count = 0
    for words in anagram_dict.values():
        if len(words) >= 2:
            anagram_count += len(list(combinations(words, 2)))
    return anagram_count >= 65