from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    count = 0
    for word1, word2 in combinations(lst, 2):
        if len(word1) < 3 or len(word2) < 3:
            continue
        if Counter(word1.lower()) == Counter(word2.lower()):
            count += 1
        if count > 40:
            return False
    return count <= 40