def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(string)
    return len(list(filter(lambda x: len(x) >= 73, anagrams.values()))) >= 73