from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            string = string.lower()
            sorted_string = ''.join(sorted(string))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    if len(anagrams) > 79:
        return False
    return True