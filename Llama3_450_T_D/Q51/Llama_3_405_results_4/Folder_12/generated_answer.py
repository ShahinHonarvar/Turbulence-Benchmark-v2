def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for string in string_list:
        string_lower = string.lower()
        if len(string_lower) >= 3 and string_lower.isalpha():
            sorted_string = ''.join(sorted(string_lower))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
            else:
                anagram_dict[sorted_string] = 1
    for value in anagram_dict.values():
        anagram_count += value * (value - 1) // 2
    return anagram_count <= 92