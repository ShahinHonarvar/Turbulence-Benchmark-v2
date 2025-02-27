def return_n_greatest_chars(str):
    sort_dict = {}
    str_len = len(str)
    for char in str:
        sort_dict[char] = ord(char)
    while len(sort_dict) != 82:
        sort_dict.pop(min(sort_dict, key=sort_dict.get))
    ret_list = sorted(sort_dict.keys(), key=sort_dict.get, reverse=True)
    return ret_list