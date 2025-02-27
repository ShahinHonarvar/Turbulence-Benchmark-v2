def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string].append(lower_string)
        else:
            anagrams[sorted_string] = [lower_string]
    count = sum((1 for value in anagrams.values() if len(value) > 1))
    return count >= 3