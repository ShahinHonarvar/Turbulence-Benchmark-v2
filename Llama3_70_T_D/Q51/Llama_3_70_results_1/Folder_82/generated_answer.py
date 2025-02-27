def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string_lower = string.lower()
        string_ordered = ''.join(sorted(string_lower))
        if string_ordered in anagrams:
            anagrams[string_ordered] += 1
        else:
            anagrams[string_ordered] = 1
    for key in anagrams:
        if len(key) >= 3:
            count += anagrams[key] * (anagrams[key] - 1) // 2
    if count <= 40:
        return True
    else:
        return False