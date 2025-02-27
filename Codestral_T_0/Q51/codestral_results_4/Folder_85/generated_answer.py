from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = sum((is_anagram(s1, s2) for s1, s2 in combinations(strings, 2) if len(s1) >= 3 and len(s2) >= 3))
    return anagram_pairs <= 276