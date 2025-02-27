def return_n_greatest_chars(s, n=2):
    return sorted([char for char in s], reverse=True)[:n]