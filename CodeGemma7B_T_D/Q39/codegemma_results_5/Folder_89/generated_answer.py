def return_n_greatest_chars(cs):
    return sorted(cs, key=ord, reverse=True)[:55]