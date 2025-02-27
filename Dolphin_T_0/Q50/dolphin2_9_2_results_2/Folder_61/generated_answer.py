from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagrams = 0
    for word1, word2 in combinations(lst, 2):
        if len(word1) >= 3 and len(word2) >= 3:
            if Counter(word1.lower()) == Counter(word2.lower()):
                anagrams += 1
    return anagrams >= 8