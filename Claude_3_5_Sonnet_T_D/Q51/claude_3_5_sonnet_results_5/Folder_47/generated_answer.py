from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        if len(str1) >= 3 and len(str2) >= 3:
            sorted_str1 = ''.join(sorted(filter(str.isalpha, str1.lower())))
            sorted_str2 = ''.join(sorted(filter(str.isalpha, str2.lower())))
            if sorted_str1 == sorted_str2 and sorted_str1:
                anagram_count += 1
                if anagram_count > 366:
                    return False
    return True