def if_contains_anagrams(strings):
    anagrams = {}
    pairs = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            pairs += anagrams[sorted_string]
        else:
            anagrams[sorted_string] = 1
    return pairs >= 10