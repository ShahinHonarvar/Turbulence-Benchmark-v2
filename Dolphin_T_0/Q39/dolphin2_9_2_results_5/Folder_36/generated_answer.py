def return_n_greatest_chars(s):
    chars = [c for c in s]
    chars.sort()
    return chars[-32:]