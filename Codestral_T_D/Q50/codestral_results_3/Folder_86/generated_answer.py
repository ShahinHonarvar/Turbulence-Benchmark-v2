def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    count = 0
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 115