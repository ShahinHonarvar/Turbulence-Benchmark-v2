from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        if len(s1) >= 3 and len(s2) >= 3:
            s1_clean = ''.join((c for c in s1.lower() if c.isalpha()))
            s2_clean = ''.join((c for c in s2.lower() if c.isalpha()))
            if s1_clean != s2_clean and is_anagram(s1_clean, s2_clean):
                anagram_count += 1
                if anagram_count > 59:
                    return False
    return True