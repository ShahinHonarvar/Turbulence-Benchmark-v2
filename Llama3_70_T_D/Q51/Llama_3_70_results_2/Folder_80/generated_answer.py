def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        string_sorted = ''.join(sorted(string_lower))
        if len(string_lower) < 3 or not string_lower.isalpha():
            continue
        if string_sorted in anagrams:
            count += anagrams[string_sorted]
            anagrams[string_sorted] += 1
        else:
            anagrams[string_sorted] = 1
    return count <= 255