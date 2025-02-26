from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(filter(str.isalpha, s1.lower())) == sorted(filter(str.isalpha, s2.lower()))
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            anagram_count += 1
            if anagram_count > 48:
                return False
    return True