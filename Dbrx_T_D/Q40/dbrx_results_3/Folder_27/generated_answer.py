def return_n_smallest_chars(input_string):
    sorted_ascii_values = sorted((ord(c) for c in input_string))
    return sorted_ascii_values[:82]