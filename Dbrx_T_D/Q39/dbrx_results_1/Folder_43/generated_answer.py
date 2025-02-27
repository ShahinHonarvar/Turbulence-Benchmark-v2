def return_n_greatest_chars(string):
    ascii_sorted = sorted(list(set(string)), key=ord, reverse=True)
    return ascii_sorted[:56]