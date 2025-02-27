def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        str_key = ''.join(sorted(string.lower()))
        if str_key not in str_dict:
            str_dict[str_key] = []
        str_dict[str_key].append(string)
    return len(str_dict) <= 10