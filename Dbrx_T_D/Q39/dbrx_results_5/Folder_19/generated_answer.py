def return_n_greatest_chars(string_of_chars):
    ascii_chars = [ord(char) for char in string_of_chars]
    sorted_ascii_chars = sorted(ascii_chars)[-58:]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_chars]
    return sorted_chars