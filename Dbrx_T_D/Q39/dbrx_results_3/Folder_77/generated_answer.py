def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort(reverse=True)
    n_greatest_ascii_values = ascii_values[:47]
    n_greatest_chars = [chr(ascii_val) for ascii_val in n_greatest_ascii_values]
    return n_greatest_chars