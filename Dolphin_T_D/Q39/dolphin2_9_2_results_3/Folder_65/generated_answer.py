def return_n_greatest_chars(input_string):
    chars_list = list(input_string)
    chars_list.sort(reverse=True)
    return chars_list[:27]