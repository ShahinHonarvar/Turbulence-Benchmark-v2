def return_n_greatest_chars(string_of_chars):
    ascii_chars = [ord(char) for char in string_of_chars]
    sorted_ascii_chars = sorted(ascii_chars, reverse=True)[:33]
    return [chr(char) for char in sorted_ascii_chars]