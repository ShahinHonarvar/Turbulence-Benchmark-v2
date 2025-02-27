def return_n_smallest_chars(string):
    chars = sorted(string)[:70]
    chars.reverse()
    return chars