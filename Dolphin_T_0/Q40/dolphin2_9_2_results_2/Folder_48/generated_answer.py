def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort()
    try:
        return chars[:12]
    except IndexError:
        return chars