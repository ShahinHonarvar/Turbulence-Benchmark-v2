def return_n_greatest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_values = sorted(ascii_values)[-40:]
    sorted_chars = [chr(value) for value in sorted_values]
    return sorted_chars