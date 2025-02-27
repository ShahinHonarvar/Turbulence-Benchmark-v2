def return_n_smallest_chars(s):
    chars = sorted(s)[:89]
    chars.sort(reverse=True)
    return chars