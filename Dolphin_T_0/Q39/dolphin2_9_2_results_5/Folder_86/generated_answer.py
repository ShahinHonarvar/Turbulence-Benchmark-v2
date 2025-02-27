def return_n_greatest_chars(s):
    s_sorted = sorted(s, key=lambda x: -ord(x))[:34]
    return sorted(s_sorted)