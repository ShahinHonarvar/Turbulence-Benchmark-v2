def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(lower_string))
        if len(lower_string) >= 3 and sorted_string.isalpha():
            if sorted_string in anagrams:
                anagrams[sorted_string].append(lower_string)
            else:
                anagrams[sorted_string] = [lower_string]
    count = 0
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count <= 474