def return_n_smallest_chars(s):
    return sorted([c for c in s if c.isascii()], key=ord, reverse=True)[:77]