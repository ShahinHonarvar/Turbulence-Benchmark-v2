def return_n_greatest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    sorted_list = sorted(ascii_list, reverse=True)[:56]
    result_list = [chr(ascii) for ascii in sorted_list]
    return result_list