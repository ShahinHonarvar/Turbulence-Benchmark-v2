def return_n_smallest_chars(input_string):
    ascii_values = [ord(c) for c in input_string]
    sorted_ascii = sorted(ascii_values)[:64]
    sorted_chars = [chr(i) for i in sorted_ascii]
    return sorted_chars