def return_n_greatest_chars(s, n=52):
    return sorted(s, key=ord, reverse=True)[:n]