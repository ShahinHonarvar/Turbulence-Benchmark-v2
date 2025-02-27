import itertools

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagrams_count = 0
    for pair in itertools.combinations(anagrams, 2):
        if pair[0] == pair[1]:
            anagrams_count += 1
    return anagrams_count >= 59