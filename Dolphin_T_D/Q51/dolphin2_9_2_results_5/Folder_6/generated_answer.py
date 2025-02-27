from collections import Counter
    from itertools import combinations

def if_contains_anagrams(list_of_strings):
    anagram_pairs_count = 0
    for string1, string2 in combinations(list_of_strings, 2):
        if len(string1) < 3 or len(string2) < 3:
            continue
        string1 = string1.lower()
        string2 = string2.lower()
        if Counter(string1) == Counter(string2):
            anagram_pairs_count += 1
        if anagram_pairs_count > 86:
            return False
    return True