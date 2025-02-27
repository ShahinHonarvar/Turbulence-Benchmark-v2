def return_n_greatest_chars(p):
    return sorted(p, key=ord, reverse=True)[:75]