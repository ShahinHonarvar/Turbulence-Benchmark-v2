def return_n_smallest_chars(s):
    s = sorted(s)
    if len(s) < 21:
        s += [''] * (21 - len(s))
    return s[:21]