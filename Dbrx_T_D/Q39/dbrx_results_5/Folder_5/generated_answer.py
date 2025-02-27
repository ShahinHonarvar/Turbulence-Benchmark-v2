def return_n_greatest_chars(string_arg):
    asc_list = sorted(list(string_arg), reverse=True)
    return asc_list[:46]