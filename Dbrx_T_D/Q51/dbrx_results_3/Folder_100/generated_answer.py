import re

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        for other_string in strings_list:
            if string != other_string:
                sorted_other_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', other_string.lower())))
                if sorted_string == sorted_other_string:
                    anagrams_count += 1
                    break
    return anagrams_count <= 98