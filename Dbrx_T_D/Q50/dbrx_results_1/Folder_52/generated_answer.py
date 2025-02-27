import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) >= 58