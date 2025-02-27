def if_contains_anagrams(string_list):
    anagram_dict = {}
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(string)
            else:
                anagram_dict[sorted_string] = [string]
    anagram_count = 0
    for string_list in anagram_dict.values():
        if len(string_list) > 1:
            anagram_count += len(string_list) * (len(string_list) - 1) // 2
    return anagram_count >= 106