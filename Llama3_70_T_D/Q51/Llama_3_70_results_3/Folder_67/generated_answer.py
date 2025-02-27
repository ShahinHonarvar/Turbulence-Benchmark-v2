from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    pairs = set()
    for word in lst:
        word = ''.join(filter(str.isalpha, word)).lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1:
            pairs.update(combinations(anagram_list, 2))
    return len(pairs) <= 5