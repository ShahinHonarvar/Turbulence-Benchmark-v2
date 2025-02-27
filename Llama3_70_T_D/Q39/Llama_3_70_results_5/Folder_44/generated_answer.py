def return_n_greatest_chars(s):
    s_sorted = sorted(s)
    return sorted(s_sorted[-73:], reverse=False)