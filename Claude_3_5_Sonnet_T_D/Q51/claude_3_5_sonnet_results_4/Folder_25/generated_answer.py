from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for s1, s2 in combinations(string_list, 2):
        s1_alpha = ''.join((c for c in s1 if c.isalpha()))
        s2_alpha = ''.join((c for c in s2 if c.isalpha()))
        if is_anagram(s1_alpha, s2_alpha):
            anagram_pairs += 1
            if anagram_pairs > 67:
                return False
    return True