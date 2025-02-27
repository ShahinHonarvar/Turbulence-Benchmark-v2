def return_n_greatest_chars(s):
    sorted_chars = sorted(s)
    return sorted(sorted_chars[-45:])