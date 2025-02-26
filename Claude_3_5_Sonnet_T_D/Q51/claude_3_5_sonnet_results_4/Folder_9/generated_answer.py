from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1_filtered = ''.join((c for c in str1 if c.isalpha()))
        str2_filtered = ''.join((c for c in str2 if c.isalpha()))
        if len(str1_filtered) >= 3 and len(str2_filtered) >= 3 and is_anagram(str1_filtered, str2_filtered):
            anagram_count += 1
            if anagram_count > 475:
                return False
    return True