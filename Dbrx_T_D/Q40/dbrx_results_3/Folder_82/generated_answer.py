def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:60]
    sorted_chars = [chr(ascii_value) for ascii_value in sorted_ascii_values]
    return sorted_chars