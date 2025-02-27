import itertools

def if_contains_anagrams(strings_list):
    anagrams = []
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    anagrams_pairs = [list(pair) for pair in itertools.combinations(anagrams, 2) if pair[0] == pair[1]]
    return len(anagrams_pairs) >= 38