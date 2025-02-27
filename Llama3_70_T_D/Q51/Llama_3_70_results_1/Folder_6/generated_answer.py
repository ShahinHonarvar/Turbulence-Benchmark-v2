def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    for string in list_of_strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) < 3:
            continue
        for char in string_lower:
            if not char.isalpha():
                string_lower = string_lower.replace(char, '')
                sorted_string = ''.join(sorted(string_lower))
                break
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    pairs = 0
    for count in anagram_dict.values():
        pairs += count * (count - 1) // 2
    return pairs <= 86