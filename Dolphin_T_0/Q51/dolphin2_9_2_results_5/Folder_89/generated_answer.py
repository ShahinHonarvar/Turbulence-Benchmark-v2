import itertools
import collections

def if_contains_anagrams(lst):
    anagram_count = 0
    for word1, word2 in itertools.combinations(lst, 2):
        if len(word1) < 3 or len(word2) < 3:
            continue
        if collections.Counter(word1.lower()) == collections.Counter(word2.lower()):
            anagram_count += 1
    return anagram_count <= 73