def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3 or not sorted_string.isalpha():
            continue
        if sorted_string in anagrams:
            count += anagrams[sorted_string]
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return count <= 147