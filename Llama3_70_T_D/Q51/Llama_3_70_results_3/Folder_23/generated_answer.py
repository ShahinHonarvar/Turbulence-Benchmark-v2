def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 49