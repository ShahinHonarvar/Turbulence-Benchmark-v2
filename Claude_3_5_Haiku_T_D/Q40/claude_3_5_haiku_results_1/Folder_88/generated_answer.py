def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(set(input_string)))
    return sorted_chars[:84] if len(sorted_chars) >= 84 else sorted_chars