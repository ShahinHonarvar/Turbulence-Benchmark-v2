def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(filter(str.isalpha, string_lower)))
        if string_sorted in anagrams:
            anagrams[string_sorted].append(string)
        else:
            anagrams[string_sorted] = [string]
    count = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return count <= 276