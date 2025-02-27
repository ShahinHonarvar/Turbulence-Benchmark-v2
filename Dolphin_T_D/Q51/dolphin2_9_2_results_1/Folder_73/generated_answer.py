from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = sum((1 for w1, w2 in combinations(lst, 2) if len(w1) >= 3 and len(w2) >= 3 and is_anagram(w1, w2)))
    return anagram_pairs <= 279