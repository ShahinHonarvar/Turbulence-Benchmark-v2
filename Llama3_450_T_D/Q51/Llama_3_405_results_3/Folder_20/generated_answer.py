def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for string in string_list:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        if len(string_lower) < 3:
            continue
        sorted_string = ''.join(sorted(string_lower))
        if sorted_string in anagram_dict:
            count += anagram_dict[sorted_string]
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    return count <= 131