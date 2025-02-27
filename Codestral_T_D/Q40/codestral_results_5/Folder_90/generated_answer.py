def return_n_smallest_chars(s):
    chars = sorted(s)[:24]
    chars.sort(reverse=True)
    return chars