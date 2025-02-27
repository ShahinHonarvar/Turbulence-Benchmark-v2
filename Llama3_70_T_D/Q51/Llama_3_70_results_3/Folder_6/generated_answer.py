def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower = string.casefold()
        cleaned = ''.join(filter(str.isalpha, lower))
        if len(cleaned) < 3:
            continue
        sorted_string = ''.join(sorted(cleaned))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    count = 0
    for strings in anagrams.values():
        count += len(strings) * (len(strings) - 1) // 2
    return count <= 86