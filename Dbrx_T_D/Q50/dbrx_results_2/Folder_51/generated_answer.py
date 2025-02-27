import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = tuple(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 2]
    return len(anagram_pairs) >= 39