def return_n_greatest_chars(str_input):
    unique_chars = sorted(set(str_input), key=ord, reverse=True)
    return unique_chars[:82]