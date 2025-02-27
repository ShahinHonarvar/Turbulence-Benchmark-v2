def return_n_smallest_chars(str_of_chars):
    ordered_chars = sorted(str_of_chars, key=ord)[:24]
    ordered_chars.sort(reverse=True)
    return ordered_chars