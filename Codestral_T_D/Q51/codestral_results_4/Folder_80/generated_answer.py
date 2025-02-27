from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = [(s1, s2) for s1, s2 in combinations(lst, 2) if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2)]
    return len(anagram_pairs) <= 255