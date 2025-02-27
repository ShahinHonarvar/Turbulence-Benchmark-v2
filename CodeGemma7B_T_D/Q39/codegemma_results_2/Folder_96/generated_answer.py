def return_n_greatest_chars(str_of_chars):
    return sorted(str_of_chars, key=ord, reverse=True)[:20]