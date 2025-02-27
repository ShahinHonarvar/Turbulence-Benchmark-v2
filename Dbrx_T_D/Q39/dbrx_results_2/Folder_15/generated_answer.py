def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string if char != ' ']
    sorted_ascii_values = sorted(ascii_values)[-57:]
    return [chr(value) for value in sorted_ascii_values]