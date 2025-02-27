import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    pairs = [pair for pair in anagrams.values() if len(pair) >= 2]
    return len(pairs) >= 36