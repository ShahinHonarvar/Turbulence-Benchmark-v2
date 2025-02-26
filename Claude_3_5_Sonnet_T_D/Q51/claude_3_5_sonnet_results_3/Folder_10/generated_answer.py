from itertools import combinations

def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(filter(str.isalpha, str1.lower())) == sorted(filter(str.isalpha, str2.lower()))
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
            anagram_count += 1
            if anagram_count > 21:
                return False
    return True