import re

def if_contains_anagrams(strings_list):
    anagrams = set()
    for string in strings_list:
        string = re.sub('[^\\w]', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) == 2 and sorted_string[0] == sorted_string[1]:
            continue
        anagrams.add(sorted_string)
    return len(anagrams) <= 44