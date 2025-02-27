from collections import Counter

def if_contains_anagrams(str_list):
    anagrams = set()
    for string in str_list:
        lower_str = sorted(string.lower())
        key = tuple(lower_str)
        if key in anagrams:
            anagrams.remove(key)
        elif len(anagrams) < 35:
            anagrams.add(key)
        else:
            return False
    return True