def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    n_greatest_chars = sorted_values[:68]
    return [chr(value) for value in n_greatest_chars]