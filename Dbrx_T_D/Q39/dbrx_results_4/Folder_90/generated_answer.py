def return_n_greatest_chars(string_chars):
    ascii_chars = [ord(char) for char in string_chars]
    sorted_ascii_chars = sorted(ascii_chars, reverse=True)[:24]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii_chars]
    return sorted_chars