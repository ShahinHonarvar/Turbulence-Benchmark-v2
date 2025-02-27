def if_contains_anagrams(list_of_strings):
    anagrams = {}
    pairs_count = 0
    for string in list_of_strings:
        string_lower = string.lower()
        string_alpha = ''.join(filter(str.isalpha, string_lower))
        if len(string_alpha) < 3:
            continue
        sorted_string = ''.join(sorted(string_alpha))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string_lower)
        else:
            anagrams[sorted_string] = [string_lower]
    for strings in anagrams.values():
        pairs_count += len(strings) * (len(strings) - 1) // 2
    return pairs_count <= 20