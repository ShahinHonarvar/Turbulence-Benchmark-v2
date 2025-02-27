def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:29]
    return sorted(sorted_chars)