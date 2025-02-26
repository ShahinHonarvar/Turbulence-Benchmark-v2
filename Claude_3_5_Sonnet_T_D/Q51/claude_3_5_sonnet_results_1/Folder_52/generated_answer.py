from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for s1, s2 in combinations(string_list, 2):
        s1_filtered = ''.join((c for c in s1 if c.isalpha()))
        s2_filtered = ''.join((c for c in s2 if c.isalpha()))
        if is_anagram(s1_filtered, s2_filtered):
            anagram_count += 1
            if anagram_count > 43:
                return False
    return True