def return_n_smallest_chars(input_string):
    ascii_vals = [ord(char) for char in input_string if ord(char) < 58]
    return sorted(ascii_vals)