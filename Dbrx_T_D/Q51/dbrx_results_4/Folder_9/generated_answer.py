def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            anagrams[string] = anagrams.get(string, 0) + 1
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) / 2
    return count <= 475