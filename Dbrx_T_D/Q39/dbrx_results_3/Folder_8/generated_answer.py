def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[-83:]
    return [chr(value) for value in sorted_ascii_values]