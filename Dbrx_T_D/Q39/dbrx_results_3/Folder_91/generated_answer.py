def return_n_greatest_chars(string_arg):
    list_of_chars = list(string_arg)
    sorted_list = sorted(list_of_chars, reverse=True)
    return sorted_list[:6]