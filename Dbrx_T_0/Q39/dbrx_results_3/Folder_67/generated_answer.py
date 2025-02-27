def return_n_greatest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_ascii_values = sorted(ascii_values)[-66:]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    return sorted_chars