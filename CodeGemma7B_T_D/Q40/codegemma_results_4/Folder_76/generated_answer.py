def return_n_smallest_chars(str_arg):
    ordered_chars = sorted(str_arg)
    return ordered_chars[:3][::-1]