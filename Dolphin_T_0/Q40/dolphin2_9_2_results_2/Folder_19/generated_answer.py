def return_n_smallest_chars(s):
    chars = [c for c in s if c.isprintable()]
    chars.sort()
    return chars[:58]