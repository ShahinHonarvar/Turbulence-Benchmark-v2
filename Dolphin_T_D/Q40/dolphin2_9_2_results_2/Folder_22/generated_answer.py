def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda x: ord(x))
    return chars[:76]