def return_n_greatest_chars(c):
    return sorted(c, key=ord, reverse=True)[:38]