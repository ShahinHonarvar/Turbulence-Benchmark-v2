def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return anagram_pairs <= 58