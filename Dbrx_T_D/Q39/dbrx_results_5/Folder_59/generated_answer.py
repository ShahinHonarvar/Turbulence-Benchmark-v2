def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    chars_list = sorted(chars_list, key=lambda char: ord(char), reverse=True)
    return chars_list[:13]