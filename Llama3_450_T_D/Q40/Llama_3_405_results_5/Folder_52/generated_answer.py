def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c))
    return ascii_sorted[:68]