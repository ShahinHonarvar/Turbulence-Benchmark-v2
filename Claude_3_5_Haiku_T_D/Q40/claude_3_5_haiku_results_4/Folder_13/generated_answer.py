def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    return sorted_chars[:31] if len(sorted_chars) >= 31 else sorted_chars