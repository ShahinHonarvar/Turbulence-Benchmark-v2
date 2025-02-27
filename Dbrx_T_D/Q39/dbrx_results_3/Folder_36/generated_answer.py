def return_n_greatest_chars(string):
    ascii_list = sorted(list(set(string)))
    return ascii_list[-32:]