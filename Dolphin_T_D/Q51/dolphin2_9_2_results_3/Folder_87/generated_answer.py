from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    lst = [s for s in lst if len(s) >= 3]
    anagrams = set()
    for s1, s2 in combinations(lst, 2):
        if is_anagram(s1, s2):
            anagrams.add((s1, s2))
    return len(anagrams) <= 392