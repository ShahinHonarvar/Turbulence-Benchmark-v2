from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_filtered = ''.join((c for c in s1 if c.isalpha()))
        s2_filtered = ''.join((c for c in s2 if c.isalpha()))
        if is_anagram(s1_filtered, s2_filtered):
            anagram_count += 1
            if anagram_count > 29:
                return False
    return True