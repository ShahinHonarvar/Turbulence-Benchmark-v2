def return_n_smallest_chars(s):
    chars = sorted(list(s), key=lambda c: ord(c))
    return chars[:76]