import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = tuple(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    count = sum((1 for value in anagrams.values() if len(value) > 1))
    return count <= 5