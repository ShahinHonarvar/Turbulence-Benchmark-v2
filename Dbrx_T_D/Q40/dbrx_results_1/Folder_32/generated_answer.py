def return_n_smallest_chars(input_string):
    ascii_list = [ord(char) for char in input_string]
    sorted_ascii_list = sorted(ascii_list)[:8]
    sorted_char_list = [chr(ascii) for ascii in sorted_ascii_list]
    return sorted_char_list