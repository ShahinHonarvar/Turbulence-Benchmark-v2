def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    n_greatest_chars = sorted_chars[-72:]
    return sorted(n_greatest_chars)