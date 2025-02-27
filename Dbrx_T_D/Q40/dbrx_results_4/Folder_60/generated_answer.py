def return_n_smallest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    sorted_list = sorted(ascii_list)[:28]
    return [chr(char) for char in sorted_list]