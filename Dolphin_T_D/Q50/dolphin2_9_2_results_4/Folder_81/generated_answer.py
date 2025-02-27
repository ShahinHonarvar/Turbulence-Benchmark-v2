def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        if len(string) < 3:
            continue
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagrams.keys():
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    pairs = 0
    for value in anagrams.values():
        if value > 1:
            pairs += value // 2
    if pairs >= 16:
        return True
    else:
        return False