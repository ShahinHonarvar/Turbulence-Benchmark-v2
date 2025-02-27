def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_ascii_values = sorted(ascii_values)[-21:]
    sorted_chars = [chr(value) for value in sorted_ascii_values]
    return sorted_chars