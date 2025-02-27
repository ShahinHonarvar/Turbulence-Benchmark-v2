def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) >= 3:
            sorted_string = ''.join(sorted(string_lower))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string_lower)
            else:
                anagrams[sorted_string] = [string_lower]
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count >= 136