def return_n_greatest_chars(given_string):
    ascii_values = [ord(char) for char in given_string]
    ascii_values.sort(reverse=True)
    greatest_chars = [chr(value) for value in ascii_values[:27]]
    return greatest_chars