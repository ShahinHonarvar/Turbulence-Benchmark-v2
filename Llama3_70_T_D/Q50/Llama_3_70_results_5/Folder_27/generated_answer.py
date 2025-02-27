def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string_lower = string.lower()
        if len(string_lower) >= 3:
            sorted_string = ''.join(sorted(string_lower))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    for key in anagrams:
        count += anagrams[key] * (anagrams[key] - 1) // 2
    return count >= 86