from collections import Counter
    from itertools import permutations

def if_contains_anagrams(l: list[str]) -> bool:
    pairs = 0
    for word1 in l:
        if len(word1) >= 3:
            for word2 in l:
                if word1 != word2 and len(word2) >= 3:
                    if Counter(word1.lower()) == Counter(word2.lower()):
                        pairs += 1
    return pairs <= 289