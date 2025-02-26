from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for str1, str2 in combinations(string_list, 2):
        if len(str1) >= 3 and len(str2) >= 3:
            if sorted(str1.lower()) == sorted(str2.lower()):
                anagram_count += 1
                if anagram_count >= 69:
                    return True
    return False