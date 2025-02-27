from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for string in list_of_strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagrams.add(sorted_string)
        if len(anagrams) > 92:
            return False
    return True