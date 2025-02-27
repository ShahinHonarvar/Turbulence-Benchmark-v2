def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: (c in s[-10:], -ord(c)))[-10:]