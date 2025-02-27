def return_n_greatest_chars(s):
    a, b = sorted(((ord(c), c) for c in s))[-2:]
    return [b, a]