def return_n_greatest_chars(string):
    chars_list = list(string)
    chars_list = sorted(set(chars_list))
    chars_list = chars_list[-3:]
    return sorted(chars_list)