def return_n_greatest_chars(s, n=2):
    return sorted(s, reverse=True)[:n]