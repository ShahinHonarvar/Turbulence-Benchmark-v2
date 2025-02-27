import re

def if_contains_anagrams(string_list):
    anagrams_count = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())) and (re.findall('(.)\\\\1+', string1.lower()) == re.findall('(.)\\\\1+', string2.lower())):
                anagrams_count += 1
                if anagrams_count >= 93:
                    return True
    return False