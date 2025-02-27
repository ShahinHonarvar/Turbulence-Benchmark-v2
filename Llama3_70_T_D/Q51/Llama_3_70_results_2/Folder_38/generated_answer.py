def if_contains_anagrams(lst):
    anagrams_count = {}
    for string in lst:
        string_lower = string.lower()
        string_no_punct = ''.join((e for e in string_lower if e.isalnum()))
        if len(string_no_punct) < 3:
            continue
        string_sorted = ''.join(sorted(string_no_punct))
        if string_sorted in anagrams_count:
            anagrams_count[string_sorted] += 1
        else:
            anagrams_count[string_sorted] = 1
    count = 0
    for value in anagrams_count.values():
        count += value * (value - 1) // 2
    return count <= 416