def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    ascii_list = sorted(ascii_list)[-32:]
    char_list = [chr(ascii) for ascii in ascii_list]
    return char_list