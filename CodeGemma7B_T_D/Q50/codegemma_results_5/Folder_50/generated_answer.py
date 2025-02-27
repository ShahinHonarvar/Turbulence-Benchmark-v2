def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            str_dict.setdefault(sorted_string, []).append(string)
    for anagrams in str_dict.values():
        if len(anagrams) >= 20:
            return True
    return False