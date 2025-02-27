def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    chars_list = [char for char in chars_list if ord(char) > 32]
    chars_list.sort(key=ord)
    return chars_list[-28:]