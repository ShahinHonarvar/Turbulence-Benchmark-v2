def return_n_smallest_chars(str_chars):
    lst_chars = sorted(str_chars, key=ord)
    return lst_chars[:40]