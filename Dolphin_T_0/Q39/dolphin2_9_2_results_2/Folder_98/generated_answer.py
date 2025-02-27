def return_n_greatest_chars(s):
    chars = sorted([c for c in s], key=lambda c: -ord(c))
    return chars[:68]