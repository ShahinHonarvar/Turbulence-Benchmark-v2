from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        if is_anagram(s1, s2):
            anagram_count += 1
            if anagram_count > 39:
                return False
    return True