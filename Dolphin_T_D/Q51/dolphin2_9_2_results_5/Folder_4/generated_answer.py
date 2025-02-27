from collections import Counter
    from itertools import groupby

def if_contains_anagrams(list_of_strings):

    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return Counter(s1) == Counter(s2)
    count = 0
    for a, b in combinations(list_of_strings, 2):
        if is_anagram(a, b):
            count += 1
    return count <= 84