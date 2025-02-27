def return_n_greatest_chars(str):
    str_set = set(str)
    str_list = sorted(str_set, key=ord, reverse=True)
    return ''.join(str_list[:68])