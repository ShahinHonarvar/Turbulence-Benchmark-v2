def return_n_greatest_chars(s):
    n = 2
    sorted_chars = sorted(s, reverse=True)[:n]
    return sorted(sorted_chars)