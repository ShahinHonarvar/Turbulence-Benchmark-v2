def if_contains_anagrams(lst):
    sorted_strings = {}
    anagram_count = 0
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in sorted_strings:
                sorted_strings[sorted_string].append(string)
            else:
                sorted_strings[sorted_string] = [string]
    for strings in sorted_strings.values():
        if len(strings) > 1:
            anagram_count += len(strings) * (len(strings) - 1) // 2
            if anagram_count >= 94:
                return True
    return False