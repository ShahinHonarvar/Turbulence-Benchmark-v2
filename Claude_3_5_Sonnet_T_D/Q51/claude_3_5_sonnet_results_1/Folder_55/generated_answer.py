from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_clean = ''.join((char.lower() for char in s1 if char.isalpha()))
        s2_clean = ''.join((char.lower() for char in s2 if char.isalpha()))
        if len(s1_clean) >= 3 and len(s2_clean) >= 3 and is_anagram(s1_clean, s2_clean):
            anagram_count += 1
            if anagram_count > 44:
                return False
    return True