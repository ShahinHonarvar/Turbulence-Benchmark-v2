def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            str_dict.setdefault(sorted_str, []).append(string)
    pairs = 0
    for anagram_list in str_dict.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs >= 70