def return_n_greatest_chars(s):
    return sorted([c for c in s if c not in '][\n\t\r' and c.isascii()][-19:])