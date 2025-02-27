def return_n_greatest_chars(s):
    chars = [c for c in s if c.isalpha()]
    chars.sort(key=lambda c: -ord(c))
    return chars[:84]