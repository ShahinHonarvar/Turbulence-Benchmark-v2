def if_contains_anagrams(lst):
    anagrams_dict = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        string_sorted = ''.join(sorted(string_lower))
        if len(string_sorted) < 3:
            continue
        if string_sorted in anagrams_dict:
            anagrams_dict[string_sorted] += 1
        else:
            anagrams_dict[string_sorted] = 1
    for value in anagrams_dict.values():
        if value > 1:
            count += 1
    return count <= 3