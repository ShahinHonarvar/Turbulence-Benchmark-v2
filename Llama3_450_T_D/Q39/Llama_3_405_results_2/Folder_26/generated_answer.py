def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c), reverse=True)
    n_greatest_chars = ascii_sorted[:43]
    return sorted(n_greatest_chars)