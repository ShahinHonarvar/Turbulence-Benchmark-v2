def return_n_greatest_chars(s):
    chars = sorted([c for c in s], key=lambda c: ord(c), reverse=True)[:29]
    return sorted(chars)