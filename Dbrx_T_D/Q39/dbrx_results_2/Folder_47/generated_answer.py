def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort(reverse=True)
    n_greatest_ascii_values = ascii_values[:21]
    return [chr(ascii_value) for ascii_value in n_greatest_ascii_values]