def return_n_smallest_chars(s):
    chars = [c for c in s if c.isalpha()]
    chars.sort()
    return chars[:52]