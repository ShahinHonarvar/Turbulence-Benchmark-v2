def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_values = sorted(ascii_values)[-64:]
    sorted_chars = [chr(value) for value in sorted_values]
    return sorted_chars