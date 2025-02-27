def return_n_smallest_chars(s):
    l = sorted([ch for ch in s], key=lambda ch: ord(ch))
    return l[:32]