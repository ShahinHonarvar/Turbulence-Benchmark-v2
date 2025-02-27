def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    return any((count >= 2 for count in anagrams.values())) and sum((count * (count - 1) // 2 for count in anagrams.values())) >= 177