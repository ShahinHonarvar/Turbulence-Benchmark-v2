def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        string_lower = ''.join(filter(str.isalpha, string.lower()))
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    pairs_count = sum((x * (x - 1) // 2 for x in anagrams_count.values()))
    return pairs_count <= 70