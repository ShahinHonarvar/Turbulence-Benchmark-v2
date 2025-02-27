def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[-34:]
    sorted_chars = [chr(value) for value in sorted_ascii_values]
    return sorted_chars