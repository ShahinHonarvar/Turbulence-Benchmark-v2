def return_n_smallest_chars(s):
    n = 28
    lowest_ascii = sorted([c for c in s if c.isascii()], key=lambda x: ord(x))[:n]
    return sorted([c for c in lowest_ascii], key=lambda x: ord(x), reverse=True)