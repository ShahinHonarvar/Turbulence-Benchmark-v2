import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagram_pairs = [list(x) for x in itertools.combinations(anagrams, 2) if x[0] == x[1]]
    return len(anagram_pairs) >= 97