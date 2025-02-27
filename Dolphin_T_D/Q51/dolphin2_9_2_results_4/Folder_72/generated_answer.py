from collections import Counter
	from itertools import combinations

def if_contains_anagrams(lst):
    candidates = [s for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for word1, word2 in combinations(candidates, 2):
        word1 = ''.join(sorted(word1.lower()))
        word2 = ''.join(sorted(word2.lower()))
        if word1 == word2:
            anagram_pairs += 1
    return anagram_pairs <= 188