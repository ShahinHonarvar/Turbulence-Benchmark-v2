def return_n_greatest_chars(s):
    n = 56
    return sorted([ch for ch in s], key=lambda ch: -ord(ch))[:n]