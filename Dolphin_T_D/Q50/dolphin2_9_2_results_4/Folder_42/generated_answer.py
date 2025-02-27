def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    anagrams = {}
    for string in list_of_strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
    for values in anagrams.values():
        n = len(values)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 233