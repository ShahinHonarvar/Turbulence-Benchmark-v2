def if_contains_anagrams(list_of_strings):
    anagrams = {}
    pairs = 0
    for string in list_of_strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
        pairs += max(0, anagrams[sorted_string] - 1)
        if pairs > 85:
            return False
    return True