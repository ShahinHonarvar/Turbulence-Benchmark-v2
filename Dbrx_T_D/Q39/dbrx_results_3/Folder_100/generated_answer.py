def return_n_greatest_chars(string_of_chars):
    chars_list = list(sorted(string_of_chars, key=ord, reverse=True))
    return chars_list[:72]