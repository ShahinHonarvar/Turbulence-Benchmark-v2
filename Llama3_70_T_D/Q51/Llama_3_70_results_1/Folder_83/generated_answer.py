def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagrams:
            anagrams[string_sorted] += 1
        else:
            anagrams[string_sorted] = 1
    for key, value in anagrams.items():
        if len(key) >= 3:
            count += value * (value - 1) // 2
    return count <= 19