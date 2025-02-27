def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values)[:60]
    return [chr(value) for value in sorted_values]