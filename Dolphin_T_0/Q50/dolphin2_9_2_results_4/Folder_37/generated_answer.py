from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for word_1, word_2 in combinations(lst, 2):
        if len(word_1) >= 3 and len(word_2) >= 3 and (Counter(word_1.lower()) == Counter(word_2.lower())):
            anagram_pairs += 1
    return anagram_pairs >= 29