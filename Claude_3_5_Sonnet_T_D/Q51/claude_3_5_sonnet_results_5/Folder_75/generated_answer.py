from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        cleaned_str1 = ''.join((char.lower() for char in str1 if char.isalpha()))
        cleaned_str2 = ''.join((char.lower() for char in str2 if char.isalpha()))
        if len(cleaned_str1) >= 3 and len(cleaned_str2) >= 3:
            if sorted(cleaned_str1) == sorted(cleaned_str2):
                anagram_count += 1
                if anagram_count > 55:
                    return False
    return True