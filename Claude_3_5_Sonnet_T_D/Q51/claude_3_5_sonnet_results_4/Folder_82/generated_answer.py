from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1_cleaned = ''.join(filter(str.isalpha, str1.lower()))
        str2_cleaned = ''.join(filter(str.isalpha, str2.lower()))
        if len(str1_cleaned) >= 3 and len(str2_cleaned) >= 3:
            if sorted(str1_cleaned) == sorted(str2_cleaned):
                anagram_count += 1
                if anagram_count > 40:
                    return False
    return True