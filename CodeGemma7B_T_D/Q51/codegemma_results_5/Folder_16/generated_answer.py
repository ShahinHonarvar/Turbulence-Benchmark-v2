def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        str_dict[sorted_string] = str_dict.get(sorted_string, 0) + 1
    anagram_count = 0
    for count in str_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 24