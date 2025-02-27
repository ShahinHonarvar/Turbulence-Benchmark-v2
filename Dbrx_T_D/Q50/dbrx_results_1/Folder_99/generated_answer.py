import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = tuple(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    pairs = sum((len(ana) * (len(ana) - 1) // 2 for ana in anagrams.values()))
    return pairs >= 314