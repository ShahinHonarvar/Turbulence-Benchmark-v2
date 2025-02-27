def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    pair_count = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return pair_count <= 17