from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s, t):
        return Counter(s.lower()) == Counter(t.lower())
    for s, t in combinations(lst, 2):
        if is_anagram(s, t) and len(s) >= 3 and (len(t) >= 3):
            return True
    return False