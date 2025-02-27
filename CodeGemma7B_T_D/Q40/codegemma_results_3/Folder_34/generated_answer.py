def return_n_smallest_chars(str_of_chars):
    str_of_chars = sorted(str_of_chars, key=ord)
    return str_of_chars[:9]