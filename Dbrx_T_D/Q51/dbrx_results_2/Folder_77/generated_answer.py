import re

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                sorted_string1 = ''.join(sorted(re.findall('\\w', string1.lower())))
                sorted_string2 = ''.join(sorted(re.findall('\\w', string2.lower())))
                if sorted_string1 == sorted_string2:
                    anagram_count += 1
                    if anagram_count > 17:
                        return False
    return True