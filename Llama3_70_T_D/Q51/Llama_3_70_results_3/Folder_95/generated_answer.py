def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_strings = {}
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        if len(string_lower) >= 3:
            sorted_string = ''.join(sorted(string_lower))
            if sorted_string in sorted_strings:
                sorted_strings[sorted_string].append(string_lower)
                anagram_count += 1
            else:
                sorted_strings[sorted_string] = [string_lower]
    return anagram_count // 2 <= 6