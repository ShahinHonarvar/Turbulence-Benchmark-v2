def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    anagram_pairs = sum((value // 2 for value in anagrams.values()))
    return anagram_pairs <= 407