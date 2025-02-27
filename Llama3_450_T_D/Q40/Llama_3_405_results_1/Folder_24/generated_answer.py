def return_n_smallest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c))
    n_smallest_chars = ascii_sorted[:32]
    return sorted(n_smallest_chars, reverse=True)