from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1_clean = ''.join(filter(str.isalpha, str1.lower()))
        str2_clean = ''.join(filter(str.isalpha, str2.lower()))
        if len(str1_clean) >= 3 and len(str2_clean) >= 3:
            if sorted(str1_clean) == sorted(str2_clean):
                anagram_count += 1
                if anagram_count > 173:
                    return False
    return True