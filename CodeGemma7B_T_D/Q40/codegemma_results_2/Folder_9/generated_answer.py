def return_n_smallest_chars(arg_string):
    sorted_chars = sorted(arg_string, key=ord)
    return sorted_chars[:20]