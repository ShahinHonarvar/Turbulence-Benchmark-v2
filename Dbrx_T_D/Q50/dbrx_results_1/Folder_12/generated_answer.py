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
    anagram_pairs = sum((len(pair) >= 2 for pair in anagrams.values()))
    return anagram_pairs >= 69