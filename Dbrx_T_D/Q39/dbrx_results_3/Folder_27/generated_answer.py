def return_n_greatest_chars(string_arg):
    chars_list = list(string_arg)
    chars_list = sorted(chars_list, key=ord)[:82]
    return chars_list