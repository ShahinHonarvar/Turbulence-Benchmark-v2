def return_n_greatest_chars(string):
    ascii_list = [ord(char) for char in string]
    sorted_ascii_list = sorted(ascii_list)[-55:]
    sorted_char_list = [chr(ascii) for ascii in sorted_ascii_list]
    return sorted_char_list