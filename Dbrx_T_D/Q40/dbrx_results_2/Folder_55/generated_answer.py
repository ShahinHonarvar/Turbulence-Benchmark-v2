def return_n_smallest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    sorted_ascii_list = sorted(ascii_list)[:75]
    sorted_ascii_list_descending = sorted(sorted_ascii_list, reverse=True)
    result = [chr(val) for val in sorted_ascii_list_descending]
    return result