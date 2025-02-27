def return_n_greatest_chars(string_of_chars):
    ascii_values = [ord(char) for char in string_of_chars]
    sorted_ascii_values = sorted(ascii_values)[-73:]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_values]
    return sorted_chars