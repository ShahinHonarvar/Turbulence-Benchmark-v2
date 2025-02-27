def return_n_greatest_chars(string):
    chars = sorted(list(set(string)), reverse=True)
    return chars[:56]