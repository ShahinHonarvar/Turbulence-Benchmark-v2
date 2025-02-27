def return_n_smallest_chars(s):
    s = sorted(list(s))
    ascii_sorted = [chr(i) for i in sorted(set(map(ord, s)))]
    n_chars = ascii_sorted[:69]
    return n_chars