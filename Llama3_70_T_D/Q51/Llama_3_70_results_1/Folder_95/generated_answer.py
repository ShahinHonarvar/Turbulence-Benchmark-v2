def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted not in anagrams:
            anagrams[string_sorted] = 0
        anagrams[string_sorted] += 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 6