def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    for count in anagrams.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 88