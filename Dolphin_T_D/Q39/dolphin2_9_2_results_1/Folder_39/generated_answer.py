def return_n_greatest_chars(s):
    chars = sorted([c for c in s if c.isalpha()], key=lambda x: -ord(x))
    return chars[:23]