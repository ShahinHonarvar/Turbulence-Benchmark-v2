from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_alpha = ''.join(filter(str.isalpha, s1))
        s2_alpha = ''.join(filter(str.isalpha, s2))
        if len(s1_alpha) >= 3 and len(s2_alpha) >= 3 and is_anagram(s1_alpha, s2_alpha):
            anagram_count += 1
            if anagram_count > 36:
                return False
    return True