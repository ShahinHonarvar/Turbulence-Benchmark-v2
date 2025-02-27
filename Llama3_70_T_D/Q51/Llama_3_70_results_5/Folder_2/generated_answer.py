def if_contains_anagrams(strings):
    anagrams_count = {}
    for string in strings:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagrams_count:
            anagrams_count[string_sorted] += 1
        else:
            anagrams_count[string_sorted] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs <= 81