def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key in str_dict:
            str_dict[key] += 1
        else:
            str_dict[key] = 1
    for count in str_dict.values():
        if count >= 49:
            return True
    return False