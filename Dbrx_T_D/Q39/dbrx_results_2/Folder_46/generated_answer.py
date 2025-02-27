def return_n_greatest_chars(s):
    ascii_sorted_chars = sorted(s, key=ord, reverse=True)
    return ascii_sorted_chars[:54]