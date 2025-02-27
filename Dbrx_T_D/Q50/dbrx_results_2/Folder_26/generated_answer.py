import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagrams_count = len(list(itertools.combinations(anagrams, 2)))
    return anagrams_count >= 49