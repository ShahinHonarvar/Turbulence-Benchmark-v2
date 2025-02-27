def if_contains_anagrams(str_list):
    str_length = len(str_list)
    if str_length < 2 * 144:
        return False
    usable_strings = [x for x in str_list if len(x) >= 3]
    usable_str_num = len(usable_strings)
    if usable_str_num < 2 * 144:
        return False
    str_dict = {}
    for string in usable_strings:
        key = ''.join(sorted(string.lower()))
        if key in str_dict:
            str_dict[key].append(string)
        else:
            str_dict[key] = [string]
    for x in str_dict.values():
        if len(x) > 1:
            return True
    return False