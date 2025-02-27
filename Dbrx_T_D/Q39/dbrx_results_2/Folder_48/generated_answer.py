def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    chars_list.sort(key=lambda x: ord(x))
    return chars_list[-12:]