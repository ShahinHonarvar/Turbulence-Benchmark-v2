from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_strings = [''.join(sorted(s.lower())) for s in string_list if len(s) >= 3]
    for str1, str2 in combinations(processed_strings, 2):
        if str1 == str2:
            anagram_count += 1
            if anagram_count > 116:
                return False
    return True