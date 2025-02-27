def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string_lower)
        else:
            anagrams[sorted_string] = [string_lower]
    pairs = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values()))
    return pairs <= 366