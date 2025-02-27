from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        if len(s1) != len(s2):
            return False
        return Counter(s1) == Counter(s2)
    count = 0
    for s1, s2 in combinations(lst, 2):
        if is_anagram(s1, s2):
            count += 1
    return count <= 66