import re

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append((string, sorted_string))
    anagram_pairs = [pair for pair in anagrams if anagrams.count(pair) > 1]
    return len(anagram_pairs) >= 39