def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:5]
    n_smallest_chars = [chr(value) for value in sorted_ascii_values]
    return n_smallest_chars