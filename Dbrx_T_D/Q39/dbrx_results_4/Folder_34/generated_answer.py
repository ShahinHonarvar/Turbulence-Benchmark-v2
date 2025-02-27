def return_n_greatest_chars(s):
    ascii_sorted = sorted([c for c in set(s)], key=ord, reverse=True)
    return ascii_sorted[:9]