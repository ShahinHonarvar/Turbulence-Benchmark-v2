import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = tuple(sorted(string.lower()))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = set()
        anagrams[sorted_string].add(string)
    anagram_pairs = sum((len(sets) * (len(sets) - 1) // 2 for sets in anagrams.values()))
    return anagram_pairs >= 36