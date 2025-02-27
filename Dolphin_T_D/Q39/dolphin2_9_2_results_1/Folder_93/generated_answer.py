def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: -x)
    return sorted_chars[:77]