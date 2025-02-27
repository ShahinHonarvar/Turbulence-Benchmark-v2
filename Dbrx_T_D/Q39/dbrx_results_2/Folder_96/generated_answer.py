def return_n_greatest_chars(string):
    ascii_values = sorted(list(set(string)), reverse=True)
    return ascii_values[:20]