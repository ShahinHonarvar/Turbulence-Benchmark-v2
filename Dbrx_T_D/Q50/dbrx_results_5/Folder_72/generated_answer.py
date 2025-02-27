import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams.values(), 2) if len(pair[0]) == len(pair[1]) and set(pair[0]) == set(pair[1])]
    return len(anagram_pairs) >= 55