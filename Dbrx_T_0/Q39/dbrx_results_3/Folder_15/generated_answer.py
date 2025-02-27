def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=ord)
    return ascii_sorted[-57:]