def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 2:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count >= 85