def return_n_smallest_chars(string_arg):
    ascii_list = sorted(list(string_arg), key=ord)
    return ascii_list[::-1][:89]