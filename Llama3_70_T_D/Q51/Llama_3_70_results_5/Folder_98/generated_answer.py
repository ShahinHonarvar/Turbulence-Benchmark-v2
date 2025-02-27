def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) >= 3 and sorted_string in anagrams:
            count += 1
        anagrams[sorted_string] = True
    return count <= 46