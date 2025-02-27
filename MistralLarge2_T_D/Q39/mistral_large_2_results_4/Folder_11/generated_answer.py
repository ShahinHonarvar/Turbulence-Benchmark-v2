def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    return sorted(sorted_chars[:17])