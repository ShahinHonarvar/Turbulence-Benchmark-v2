def return_n_smallest_chars(s):
    chars = sorted(s)[:38]
    chars.sort(reverse=True)
    return chars