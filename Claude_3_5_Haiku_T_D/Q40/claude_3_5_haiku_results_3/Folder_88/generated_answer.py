def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string)
    return sorted_chars[:84] if len(input_string) >= 84 else sorted_chars