import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        sorted_string = tuple(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    anagram_pairs = [pair for pair in itertools.combinations(anagrams.values(), 2) if len(set(''.join(pair[0]) + ''.join(pair[1]))) == len(pair[0][0]) + len(pair[1][0])]
    return len(anagram_pairs) >= 94