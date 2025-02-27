def return_n_greatest_chars(s):
    s_sorted = sorted(s, reverse=True)
    return sorted(s_sorted[:60])