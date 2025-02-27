def return_n_greatest_chars(char_list):
    greatest_chars = sorted(char_list, key=ord, reverse=True)[:59]
    return greatest_chars