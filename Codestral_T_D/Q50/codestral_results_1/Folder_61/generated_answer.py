def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                anagram_count += anagrams[sorted_string]
            else:
                anagrams[sorted_string] = 0
    return anagram_count >= 8