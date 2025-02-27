def return_n_greatest_chars(s):
    ascii_sorted_chars = sorted(list(set(s)), key=ord, reverse=True)
    return ascii_sorted_chars[:56]