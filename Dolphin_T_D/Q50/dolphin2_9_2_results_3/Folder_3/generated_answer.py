from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word1, word2 in combinations(lst, 2):
        if len(word1) >= 3 and len(word2) >= 3 and (word1.lower() != word2.lower()):
            c1 = Counter(word1.lower())
            c2 = Counter(word2.lower())
            if c1 == c2:
                anagram_pairs += 1
    return anagram_pairs >= 30