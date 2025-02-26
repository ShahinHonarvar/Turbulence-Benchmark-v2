from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        str1 = ''.join(filter(str.isalpha, str1.lower()))
        str2 = ''.join(filter(str.isalpha, str2.lower()))
        if len(str1) >= 3 and len(str2) >= 3:
            if sorted(str1) == sorted(str2):
                anagram_count += 1
                if anagram_count > 255:
                    return False
    return True