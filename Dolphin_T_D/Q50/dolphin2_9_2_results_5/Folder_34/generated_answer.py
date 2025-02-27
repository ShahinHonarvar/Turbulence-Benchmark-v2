from collections import Counter
    from itertools import permutations, combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    lst = [s for s in lst if len(s) >= 3]
    pairs = [(s1, s2) for s1, s2 in combinations(lst, 2) if is_anagram(s1, s2)]
    return len(pairs) >= 25