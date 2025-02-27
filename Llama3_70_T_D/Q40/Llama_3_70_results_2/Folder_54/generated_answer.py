def return_n_smallest_chars(s):
    s = sorted(s)
    if len(s) < 79:
        return sorted(s, reverse=True)
    else:
        return sorted(s[:79], reverse=True)