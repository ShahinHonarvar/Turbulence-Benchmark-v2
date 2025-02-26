def return_n_smallest_chars(s):
    char_list = sorted(set(s))[:76]
    return char_list if len(char_list) == 76 else char_list + [chr(0)] * (76 - len(char_list))