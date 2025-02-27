def return_n_greatest_chars(string_of_chars):
    ascii_chars = [ord(char) for char in string_of_chars]
    ascii_chars.sort(reverse=True)
    n_greatest_chars = [chr(char) for char in ascii_chars[:44]]
    return n_greatest_chars