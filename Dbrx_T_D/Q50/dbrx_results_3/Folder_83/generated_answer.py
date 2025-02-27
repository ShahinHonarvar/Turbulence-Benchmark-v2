import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagram_pairs = [list(x) for x in itertools.combinations(anagrams, 2) if x[0] == x[1]]
    return len(anagram_pairs) >= 48