def return_n_greatest_chars(s):
    chars = sorted([c for c in s], key=lambda x: -ord(x))
    return sorted(chars[:69])