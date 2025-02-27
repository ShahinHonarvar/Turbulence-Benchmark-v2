def return_n_greatest_chars(s):
    desc_sorted_chars = sorted(set(s), key=lambda x: -ord(x))
    return sorted(desc_sorted_chars[:19])