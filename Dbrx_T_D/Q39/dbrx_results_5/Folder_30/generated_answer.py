def return_n_greatest_chars(input_string):
    ascii_values = [ord(char) for char in input_string]
    ascii_values.sort(reverse=True)
    n_greatest_chars = [chr(value) for value in ascii_values[:72]]
    return n_greatest_chars