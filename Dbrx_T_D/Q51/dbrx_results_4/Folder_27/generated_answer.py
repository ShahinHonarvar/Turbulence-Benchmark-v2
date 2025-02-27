import re

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 == string2:
                continue
            if len(string1) < 3 or len(string2) < 3:
                continue
            if sorted(string1.lower()) == sorted(string2.lower()):
                anagram_pairs += 1
                if anagram_pairs > 112:
                    return True
    return False