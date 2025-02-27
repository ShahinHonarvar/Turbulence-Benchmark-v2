def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    greatest_chars = [char for char, ascii in sorted(zip(input_string, ascii_values), key=lambda x: x[1], reverse=True)[:33]]
    return greatest_chars