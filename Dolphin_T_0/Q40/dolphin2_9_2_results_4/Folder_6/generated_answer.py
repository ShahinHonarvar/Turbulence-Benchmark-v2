def return_n_smallest_chars(s):
    oldest_chars = sorted(s, key=lambda c: -ord(c))
    return oldest_chars[:47]