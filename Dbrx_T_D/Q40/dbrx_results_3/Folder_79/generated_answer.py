def return_n_smallest_chars(input_string):
    ascii_values = sorted((ord(c) for c in set(input_string)))[:82]
    return [chr(v) for v in reversed(ascii_values)]