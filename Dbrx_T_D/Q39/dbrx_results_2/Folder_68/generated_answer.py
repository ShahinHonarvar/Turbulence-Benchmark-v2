def return_n_greatest_chars(string_arg):
    char_list = sorted(list(string_arg))[-89:]
    return char_list[::-1]