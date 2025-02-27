def return_n_greatest_chars(string_arg):
    return sorted(list(string_arg), key=ord, reverse=True)[:75]