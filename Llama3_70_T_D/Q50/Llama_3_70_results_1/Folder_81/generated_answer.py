def if_contains_anagrams(strings):
    anagrams = {}
    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagram_pairs += anagrams[sorted_string]
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    return anagram_pairs >= 16