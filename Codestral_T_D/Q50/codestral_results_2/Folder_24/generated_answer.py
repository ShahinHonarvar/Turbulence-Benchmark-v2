def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for values in anagrams.values():
        if len(values) >= 2:
            count += len(values) * (len(values) - 1) // 2
    return count >= 65