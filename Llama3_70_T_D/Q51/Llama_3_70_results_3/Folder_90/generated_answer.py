def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string_lower)
            else:
                anagrams[sorted_string] = [string_lower]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 147