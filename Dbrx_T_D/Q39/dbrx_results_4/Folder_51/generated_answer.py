def return_n_greatest_chars(string_of_chars):
    ascii_list = [ord(char) for char in string_of_chars]
    sorted_ascii_list = sorted(ascii_list, reverse=True)[:45]
    sorted_chars_list = [chr(ascii) for ascii in sorted_ascii_list]
    return sorted_chars_list