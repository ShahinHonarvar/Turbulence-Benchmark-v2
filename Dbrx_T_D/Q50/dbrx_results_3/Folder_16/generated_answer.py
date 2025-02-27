import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))[::-1]
            anagrams.append(sorted_string)
    anagram_pairs = [pair for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagram_pairs) >= 155