def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for value in anagrams.values():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
    return count >= 24