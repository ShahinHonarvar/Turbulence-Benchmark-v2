def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for value in anagrams.values():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 92