def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda c: ord(c))[:57]
    return chars