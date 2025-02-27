def return_n_greatest_chars(s):
    return ''.join(sorted([c for c in s if c.isascii()]))