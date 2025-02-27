def return_n_smallest_chars(str):
    str_list = sorted(list(str), key=ord)
    return str_list[:40]