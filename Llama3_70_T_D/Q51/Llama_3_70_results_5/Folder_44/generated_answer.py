def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string_lower = string.lower()
        string_filtered = ''.join(filter(str.isalpha, string_lower))
        if len(string_filtered) < 3:
            continue
        sorted_string = ''.join(sorted(string_filtered))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count = sum((value * (value - 1) // 2 for value in anagrams.values()))
    return count <= 75