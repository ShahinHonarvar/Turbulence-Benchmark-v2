def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(input_string))
    return sorted_chars[:55] if len(sorted_chars) >= 55 else sorted_chars