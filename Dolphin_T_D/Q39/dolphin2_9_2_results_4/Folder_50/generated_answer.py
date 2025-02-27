def return_n_greatest_chars(s):
    max_chars = sorted(s, key=lambda x: -ord(x))[:16]
    return max_chars