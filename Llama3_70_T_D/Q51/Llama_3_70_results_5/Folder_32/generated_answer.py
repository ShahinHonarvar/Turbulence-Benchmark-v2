def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3 or not string_lower.isalpha():
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    pairs = 0
    for anagram in anagrams.values():
        if len(anagram) > 1:
            pairs += len(anagram) * (len(anagram) - 1) // 2
    return pairs <= 89