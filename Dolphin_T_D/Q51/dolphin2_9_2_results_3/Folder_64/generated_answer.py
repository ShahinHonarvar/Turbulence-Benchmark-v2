def if_contains_anagrams(list_of_strings):
    string_map = {}
    for string in list_of_strings:
        lower_str = string.lower()
        if len(lower_str) >= 3:
            sorted_str = ''.join(sorted(lower_str))
            if sorted_str not in string_map:
                string_map[sorted_str] = [string]
            else:
                string_map[sorted_str].append(string)
    anagram_count = 0
    for key in string_map:
        if len(string_map[key]) > 1:
            pairs = len(string_map[key]) * (len(string_map[key]) - 1) // 2
            anagram_count += pairs
    return anagram_count <= 59