import itertools

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        string = ''.join(sorted(string.lower()))
        if len(string) < 3:
            continue
        anagrams.add(string)
    return len(anagrams) <= 73