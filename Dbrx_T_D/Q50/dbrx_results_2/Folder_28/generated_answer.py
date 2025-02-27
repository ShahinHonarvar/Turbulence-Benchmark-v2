import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_pairs = list(itertools.combinations(anagrams, 2))
    return len(anagram_pairs) >= 81