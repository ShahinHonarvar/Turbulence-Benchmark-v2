import itertools
import string

def if_contains_anagrams(string_list):
    anagrams = {}
    english_letters = set(string.ascii_letters.lower())
    for string in string_list:
        string = string.lower()
        if len(string) < 3 or len(set(string) & english_letters) < 2:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if sum(anagrams.values()) > 464:
                return True
        else:
            anagrams[sorted_string] = 1
    return False