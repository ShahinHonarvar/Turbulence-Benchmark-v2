def return_n_greatest_chars(char_string):
    n = 12
    return sorted(char_string, key=ord, reverse=True)[:n]