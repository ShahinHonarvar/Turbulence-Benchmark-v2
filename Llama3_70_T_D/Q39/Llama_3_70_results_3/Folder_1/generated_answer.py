def return_n_greatest_chars(s):
    n = 11
    greatest_chars = sorted(s, key=lambda c: ord(c), reverse=True)[:n]
    return greatest_chars