def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: c.lower())[:34]