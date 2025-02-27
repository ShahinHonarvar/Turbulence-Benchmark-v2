def return_n_smallest_chars(input_str):
    ascii_vals = [ord(char) for char in input_str]
    sorted_ascii_vals = sorted(ascii_vals)[:61]
    result = [chr(val) for val in sorted_ascii_vals[::-1]]
    return result