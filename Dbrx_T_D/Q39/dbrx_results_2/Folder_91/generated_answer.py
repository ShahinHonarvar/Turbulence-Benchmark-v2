def return_n_greatest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    sorted_list = sorted(ascii_list, reverse=True)[:6]
    result = [chr(i) for i in sorted_list]
    return result