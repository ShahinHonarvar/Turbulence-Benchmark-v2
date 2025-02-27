def return_n_smallest_chars(s):
    ascii_sorted = sorted(list(s), key=ord)
    return ascii_sorted[:40]