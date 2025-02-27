def return_n_greatest_chars(s):
    ascii_values = sorted(list(set(s)), reverse=True)
    return ascii_values[:52]