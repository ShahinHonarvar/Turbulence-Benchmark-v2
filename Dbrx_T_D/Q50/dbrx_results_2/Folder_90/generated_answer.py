def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    pairs = 0
    for count in anagrams.values():
        pairs += count // 2
    return pairs >= 177