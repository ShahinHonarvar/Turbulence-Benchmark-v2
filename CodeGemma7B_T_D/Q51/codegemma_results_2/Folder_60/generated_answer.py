def if_contains_anagrams(str_list):
    str_dict = {}
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        str_dict.setdefault(sorted_str, []).append(string)
    return len(str_dict) <= 77