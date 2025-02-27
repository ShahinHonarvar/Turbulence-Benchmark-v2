import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 2]
    return len(anagram_pairs) >= 14