def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for key in anagrams:
        count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count <= 445