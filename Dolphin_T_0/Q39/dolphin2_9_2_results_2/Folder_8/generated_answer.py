def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: -ord(x))
    return sorted(sorted_chars[:83])