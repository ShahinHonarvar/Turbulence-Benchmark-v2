def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams_count:
            anagrams_count[sorted_string] += 1
        else:
            anagrams_count[sorted_string] = 1
    count = 0
    for value in anagrams_count.values():
        count += value * (value - 1) // 2
    return count <= 57