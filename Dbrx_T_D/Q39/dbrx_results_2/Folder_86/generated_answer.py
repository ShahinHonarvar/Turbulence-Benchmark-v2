def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    sorted_ascii_values = sorted(ascii_values)[:34]
    return [chr(ascii) for ascii in sorted_ascii_values]