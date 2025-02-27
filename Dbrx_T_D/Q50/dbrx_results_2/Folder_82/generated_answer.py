import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = tuple(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(x) * (len(x) - 1) // 2 for x in anagrams.values()))
    return anagram_pairs >= 276