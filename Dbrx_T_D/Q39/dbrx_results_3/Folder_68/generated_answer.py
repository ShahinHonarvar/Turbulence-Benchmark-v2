def return_n_greatest_chars(string_arg):
    ascii_list = [ord(char) for char in string_arg]
    ascii_list.sort(reverse=True)
    n_greatest_chars = [chr(ascii) for ascii in ascii_list[:89]]
    return n_greatest_chars