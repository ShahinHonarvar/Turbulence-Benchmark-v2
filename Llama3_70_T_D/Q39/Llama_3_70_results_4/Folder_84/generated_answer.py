def return_n_greatest_chars(s, n=10):
    return sorted(sorted(s)[-n:])