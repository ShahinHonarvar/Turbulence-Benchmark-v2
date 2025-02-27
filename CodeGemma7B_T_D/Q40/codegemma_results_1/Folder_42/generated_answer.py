def return_n_smallest_chars(string):
    ordered_chars_list = sorted(string, key=ord, reverse=True)
    return ordered_chars_list[:59]