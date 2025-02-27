def return_n_smallest_chars(input_string):
    ascii_sorted_chars = sorted(input_string, key=ord)
    n_smallest_chars = ascii_sorted_chars[:66]
    return n_smallest_chars