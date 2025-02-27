def if_contains_anagrams(strings):
    pairs_of_anagrams = 0
    anagrams = {}
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                continue
            anagrams[sorted_string] = 1
        else:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
        pairs_of_anagrams += anagrams[sorted_string] // 2
    return pairs_of_anagrams <= 73