def return_n_smallest_chars(input_string):
    sorted_chars = sorted(set(input_string))
    return sorted_chars[:28] if len(sorted_chars) >= 28 else sorted_chars