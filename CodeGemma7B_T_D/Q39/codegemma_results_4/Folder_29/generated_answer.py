def return_n_greatest_chars(str_chars):
    return sorted(str_chars, key=ord, reverse=True)[:23]