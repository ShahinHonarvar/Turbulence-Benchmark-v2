def return_n_greatest_chars(string_arg):
    sorted_list = sorted(list(string_arg), key=ord)
    return sorted_list[-28:]