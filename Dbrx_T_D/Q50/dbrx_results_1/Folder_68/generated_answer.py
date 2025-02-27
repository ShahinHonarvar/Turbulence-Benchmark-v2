def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, []) + [string]
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            count += len(anagram) - 1
    return count >= 9