def return_n_smallest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    ascii_list.sort()
    n_small_ascii = ascii_list[:35]
    n_small_chars = [chr(ascii) for ascii in n_small_ascii]
    return n_small_chars