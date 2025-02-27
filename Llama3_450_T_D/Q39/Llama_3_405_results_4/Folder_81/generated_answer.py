def return_n_greatest_chars(s):
    s = sorted(s, key=lambda c: ord(c), reverse=True)[:64]
    return sorted(s)