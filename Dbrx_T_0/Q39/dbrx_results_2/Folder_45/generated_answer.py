def return_n_greatest_chars(s):
    ascii_values = [ord(char) for char in s]
    sorted_ascii_values = sorted(ascii_values)[-52:]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    return sorted_chars