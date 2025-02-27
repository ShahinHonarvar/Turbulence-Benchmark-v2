from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for pair in combinations(lst, 2):
        if len(pair[0]) >= 3 and sorted(pair[0].lower()) == sorted(pair[1].lower()):
            anagram_pairs += 1
            if anagram_pairs > 86:
                return False
    return True