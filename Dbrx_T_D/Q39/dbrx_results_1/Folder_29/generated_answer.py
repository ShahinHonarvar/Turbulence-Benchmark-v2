def return_n_greatest_chars(string_of_chars):
    ascii_chars = [ord(char) for char in string_of_chars]
    sorted_ascii = sorted(ascii_chars, reverse=True)[:23]
    sorted_chars = [chr(ascii) for ascii in sorted_ascii]
    return sorted_chars