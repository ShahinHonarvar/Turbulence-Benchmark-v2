import re

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                string1 = re.sub('[^\\w]', '', string1).lower()
                string2 = re.sub('[^\\w]', '', string2).lower()
                sorted_string1 = ''.join(sorted(string1))
                sorted_string2 = ''.join(sorted(string2))
                if sorted_string1 == sorted_string2:
                    anagrams_count += 1
    return anagrams_count <= 474