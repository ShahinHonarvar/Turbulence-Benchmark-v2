def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        if len(string) < 5:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        str_dict.setdefault(sorted_string, []).append(string)
    return any((len(anagrams) >= 19 for anagrams in str_dict.values()))