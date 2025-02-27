from collections import Counter

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    anagram_pairs = sum((value // 2 for value in anagrams.values()))
    return anagram_pairs >= 78