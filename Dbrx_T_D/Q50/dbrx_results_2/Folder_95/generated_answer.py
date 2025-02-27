import itertools

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    numberOfPairs = sum((sum((1 for j in itertools.islice(anagrams, i, None) if anagrams.count(j) >= 2)) for i, j in enumerate(anagrams)))
    if numberOfPairs >= 93:
        return True
    else:
        return False