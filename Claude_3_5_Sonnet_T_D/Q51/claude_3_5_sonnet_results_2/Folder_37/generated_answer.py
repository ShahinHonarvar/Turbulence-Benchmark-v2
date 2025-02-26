from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1_filtered = ''.join(filter(str.isalpha, str1.lower()))
        str2_filtered = ''.join(filter(str.isalpha, str2.lower()))
        if len(str1_filtered) >= 3 and len(str2_filtered) >= 3:
            if sorted(str1_filtered) == sorted(str2_filtered):
                anagram_count += 1
                if anagram_count > 206:
                    return False
    return True