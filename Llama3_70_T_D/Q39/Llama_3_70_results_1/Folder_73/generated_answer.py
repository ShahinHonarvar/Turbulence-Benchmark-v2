def return_n_greatest_chars(s):
    sorted_s = sorted(s)
    n_greatest_chars = sorted_s[-80:]
    return sorted(n_greatest_chars)