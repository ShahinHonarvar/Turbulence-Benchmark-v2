def return_n_smallest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:69]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    return sorted_chars