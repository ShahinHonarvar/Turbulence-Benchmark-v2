def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda c: -ord(c))
    return sorted(sorted_chars[:3])