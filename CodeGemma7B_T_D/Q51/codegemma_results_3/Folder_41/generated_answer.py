def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            str_dict.setdefault(sorted_string, []).append(string)
    anagram_pairs = 0
    for anagram_list in str_dict.values():
        anagram_pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_pairs <= 52