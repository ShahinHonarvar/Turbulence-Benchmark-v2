def return_n_greatest_chars(string):
    n = 77
    return sorted(string, key=ord, reverse=True)[:n]