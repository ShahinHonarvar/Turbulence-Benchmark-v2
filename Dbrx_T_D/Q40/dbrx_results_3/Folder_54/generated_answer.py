def return_n_smallest_chars(string_):
    ascii_sorted_chars = sorted(list(string_), key=ord)
    return ascii_sorted_chars[-79:] if len(ascii_sorted_chars) > 79 else ascii_sorted_chars