def if_contains_anagrams(str_list):
    str_dict = {}
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower()))
        if len(sorted_str) >= 3:
            str_dict.setdefault(sorted_str, []).append(str)
    return len(str_dict) <= 257