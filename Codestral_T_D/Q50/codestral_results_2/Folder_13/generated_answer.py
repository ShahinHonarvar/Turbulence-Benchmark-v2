def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    return len([value for value in anagrams.values() if value >= 2]) >= 72