import itertools

def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(string)
    for group in anagrams.values():
        if len(group) >= 97:
            return True
    return False