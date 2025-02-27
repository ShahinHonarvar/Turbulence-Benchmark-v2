import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) <= 75