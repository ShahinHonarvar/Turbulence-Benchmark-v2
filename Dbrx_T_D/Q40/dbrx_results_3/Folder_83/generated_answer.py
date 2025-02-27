def return_n_smallest_chars(input_string):
    ascii_vals = [ord(char) for char in input_string]
    sorted_ascii_vals = sorted(ascii_vals)[:38]
    sorted_chars = [chr(val) for val in sorted_ascii_vals]
    return sorted_chars[::-1]