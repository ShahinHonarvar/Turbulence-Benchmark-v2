def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagrams:
            anagrams[string_sorted] += 1
        else:
            anagrams[string_sorted] = 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count <= 41