def return_n_greatest_chars(char_string):
    return sorted(char_string, key=ord, reverse=False)[:48]