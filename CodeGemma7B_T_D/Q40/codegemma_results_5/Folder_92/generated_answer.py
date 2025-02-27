def return_n_smallest_chars(str_in):
    return sorted(str_in, key=lambda x: ord(x))[:63]