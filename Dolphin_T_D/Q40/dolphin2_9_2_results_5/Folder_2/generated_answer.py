def return_n_smallest_chars(s):
    chars = sorted([c for c in s], key=lambda x: ord(x))
    return chars[:48]