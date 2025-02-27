from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    pairs = 0
    for word1, word2 in combinations(lst, 2):
        word1 = word1.lower()
        word2 = word2.lower()
        if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
            pairs += 1
    return pairs >= 64