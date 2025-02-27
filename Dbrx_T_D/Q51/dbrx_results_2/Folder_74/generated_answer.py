def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string] = anagrams.get(sorted_string, 0) + 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams <= 57