def return_n_greatest_chars(string_of_chars):
    chars_list = list(string_of_chars)
    chars_list.sort(key=lambda char: ord(char), reverse=True)
    return chars_list[:84]