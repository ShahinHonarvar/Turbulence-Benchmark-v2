def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    str_dict = {}
    for str_val in str_list:
        str_key = ''.join(sorted(str_val.lower()))
        if str_key in str_dict:
            str_dict[str_key] += 1
        else:
            str_dict[str_key] = 1
    str_pairs = 0
    for k, v in str_dict.items():
        str_pairs += v * (v - 1) // 2
    return str_pairs <= 84