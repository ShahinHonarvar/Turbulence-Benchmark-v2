import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams.append(string)
    anagram_pairs = sum((len(list(group)) > 1 for group in itertools.groupby(sorted(anagrams))))
    return anagram_pairs <= 474