def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    anagram_count = 0
    for string in list_of_strings:
        string_lower = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string_lower)
        else:
            anagram_dict[sorted_string] = [string_lower]
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 188