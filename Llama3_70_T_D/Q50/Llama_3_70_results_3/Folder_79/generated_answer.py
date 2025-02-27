def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string_lower)
        else:
            anagrams[sorted_string] = [string_lower]
    for values in anagrams.values():
        if len(values) > 1 and len(values[0]) >= 3:
            count += len(values) * (len(values) - 1) // 2
    return count >= 40