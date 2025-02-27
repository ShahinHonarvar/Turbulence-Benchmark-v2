import itertools

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    return len(anagrams) <= 55