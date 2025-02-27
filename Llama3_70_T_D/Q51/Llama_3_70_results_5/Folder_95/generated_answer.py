def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_dict = {}
    for string in lst:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3 or not sorted_string.isalpha():
            continue
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string].append(string_lower)
        else:
            anagrams_dict[sorted_string] = [string_lower]
    for value in anagrams_dict.values():
        anagrams_count += len(value) * (len(value) - 1) // 2
    return anagrams_count <= 6