import re

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                sorted_string1 = ''.join(sorted(re.findall('\\w', string1.lower())))
                sorted_string2 = ''.join(sorted(re.findall('\\w', string2.lower())))
                if sorted_string1 == sorted_string2:
                    anagrams_count += 1
                    if anagrams_count > 54:
                        return False
    return True