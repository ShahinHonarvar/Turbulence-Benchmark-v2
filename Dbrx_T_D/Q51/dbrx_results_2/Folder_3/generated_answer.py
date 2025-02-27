import re

def if_contains_anagrams(strings):
    anagrams = {}
    max_pairs = 66
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = [string]
        else:
            anagrams[sorted_string].append(string)
    pairs = 0
    for anagram in anagrams.values():
        if len(anagram) > 1:
            pairs += len(anagram) - 1
    return pairs <= max_pairs