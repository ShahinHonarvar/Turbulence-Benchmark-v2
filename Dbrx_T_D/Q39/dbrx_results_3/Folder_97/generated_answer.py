def return_n_greatest_chars(s):
    ascii_list = [ord(char) for char in s]
    sorted_ascii_list = sorted(ascii_list)[-38:]
    sorted_char_list = [chr(ascii) for ascii in sorted_ascii_list]
    return sorted_char_list