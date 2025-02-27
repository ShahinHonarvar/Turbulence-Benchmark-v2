def return_n_greatest_chars(s):
    return sorted(s[-55:], key=lambda x: -ord(x))