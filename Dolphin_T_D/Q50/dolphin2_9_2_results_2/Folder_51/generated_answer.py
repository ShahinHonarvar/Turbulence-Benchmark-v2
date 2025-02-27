from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word1, word2 in combinations(lst, 2):
        if len(word1) < 3 or len(word2) < 3:
            continue
        if sorted(word1.lower()) == sorted(word2.lower()):
            anagram_pairs += 1
    return anagram_pairs >= 39