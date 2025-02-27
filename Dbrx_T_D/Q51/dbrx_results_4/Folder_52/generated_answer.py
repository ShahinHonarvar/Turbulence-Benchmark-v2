import re

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                string1 = re.findall('[a-z]', string1.lower())
                string2 = re.findall('[a-z]', string2.lower())
                if sorted(string1) == sorted(string2):
                    anagram_pairs += 1
                    if anagram_pairs > 43:
                        return False
    return True