def if_contains_anagrams(str_list):
    anagram_pairs = 0
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string not in str_dict:
            str_dict[sorted_string] = set()
        str_dict[sorted_string].add(string)
    for strings in str_dict.values():
        anagram_pairs += len(strings) * (len(strings) - 1) // 2
    return anagram_pairs <= 392