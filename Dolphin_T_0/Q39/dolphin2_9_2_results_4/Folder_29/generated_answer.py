def return_n_greatest_chars(s):
    desc_sorted_chars = sorted(s, key=lambda c: -ord(c))
    return desc_sorted_chars[:23]