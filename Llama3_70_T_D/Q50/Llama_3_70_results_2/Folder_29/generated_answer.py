def if_contains_anagrams(lst):
    anagram_count = 0
    anagrams = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for anagram in anagrams.values():
        anagram_count += len(anagram) * (len(anagram) - 1) // 2
    return anagram_count >= 35