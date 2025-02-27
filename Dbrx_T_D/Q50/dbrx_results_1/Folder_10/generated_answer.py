import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagrams_count = len(anagrams)
    unique_anagrams = set(anagrams)
    pairs_of_anagrams = sum((len(list(group)) > 1 for group in itertools.groupby(sorted(unique_anagrams))))
    return pairs_of_anagrams >= 52