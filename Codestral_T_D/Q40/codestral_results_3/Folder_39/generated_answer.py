def return_n_smallest_chars(s):
    if len(s) > 23:
        s = sorted(s)[:23]
    else:
        s = sorted(s)
    return s