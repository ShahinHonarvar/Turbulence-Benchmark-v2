import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    pairs = len(list(itertools.combinations(anagrams, 2)))
    return pairs >= 50