def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_sorted = ''.join(sorted(string.lower()))
        if string_sorted in anagrams:
            anagrams[string_sorted] += 1
        else:
            anagrams[string_sorted] = 1
    for value in anagrams.values():
        if value > 1:
            count += value * (value - 1) // 2
    return count <= 4