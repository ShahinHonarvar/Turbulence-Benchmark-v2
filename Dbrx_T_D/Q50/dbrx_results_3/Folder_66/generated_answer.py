import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagrams_count = sum((1 for _ in itertools.combinations(anagrams, 2) if _[0] == _[1]))
    return anagrams_count >= 92