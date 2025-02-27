def return_n_greatest_chars(s):
    greatest_chars = sorted(s, key=lambda x: -ord(x))[:64]
    return sorted(greatest_chars)