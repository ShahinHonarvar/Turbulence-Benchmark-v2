def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            str_dict.setdefault(sorted_str, []).append(string)
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 73:
            return True
    return False