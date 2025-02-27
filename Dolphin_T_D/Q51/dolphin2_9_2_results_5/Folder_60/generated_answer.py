from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    for word1, word2 in combinations(strings, 2):
        lower1 = word1.lower()
        lower2 = word2.lower()
        if len(lower1) >= 3 and len(lower2) >= 3 and (Counter(lower1) == Counter(lower2)):
            count += 1
    return count <= 77