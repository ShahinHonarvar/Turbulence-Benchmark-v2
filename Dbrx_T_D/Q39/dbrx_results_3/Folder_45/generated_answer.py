def return_n_greatest_chars(input_string):
    ascii_vals = [ord(char) for char in input_string]
    sorted_ascii = sorted(ascii_vals)[-52:]
    sorted_chars = [chr(val) for val in sorted_ascii]
    return sorted_chars