def return_n_smallest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    sorted_ascii_list = sorted(ascii_list)[:8]
    sorted_char_list = [chr(ascii) for ascii in sorted_ascii_list]
    return sorted_char_list