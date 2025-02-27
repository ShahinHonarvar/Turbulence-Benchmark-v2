import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    pairs = sum((len(list(g)) >= 2 for _, g in itertools.groupby(sorted(anagrams))))
    return pairs >= 48