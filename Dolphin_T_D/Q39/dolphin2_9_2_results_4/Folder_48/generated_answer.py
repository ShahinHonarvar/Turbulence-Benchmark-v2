def return_n_greatest_chars(input_string):
    ascii_values = sorted(map(ord, set(input_string)), reverse=True)
    greatest_chars = [chr(val) for val in ascii_values[:12]]
    greatest_chars.sort()
    return greatest_chars