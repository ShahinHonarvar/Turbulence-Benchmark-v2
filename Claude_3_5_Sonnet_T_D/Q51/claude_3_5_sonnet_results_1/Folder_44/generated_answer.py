from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for s1, s2 in combinations(string_list, 2):
        s1_letters = ''.join((c for c in s1 if c.isalpha()))
        s2_letters = ''.join((c for c in s2 if c.isalpha()))
        if len(s1_letters) >= 3 and len(s2_letters) >= 3 and is_anagram(s1_letters, s2_letters):
            anagram_pairs += 1
            if anagram_pairs > 75:
                return False
    return True