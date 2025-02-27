from collections import Counter

def if_contains_anagrams(lst):
    n = 0
    for word1 in lst:
        if len(word1) >= 3:
            for word2 in lst:
                if len(word2) >= 3 and word1 != word2:
                    if Counter(word1.lower()) == Counter(word2.lower()):
                        n += 1
    return n >= 277