from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    anagram_pairs = sum((is_anagram(s1, s2) for s1, s2 in combinations(lst, 2) if len(s1) >= 3 and len(s2) >= 3))
    return anagram_pairs <= 289