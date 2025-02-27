def return_n_greatest_chars(s):
    sorted_chars = sorted(list(s), key=lambda x: -ord(x))
    return sorted_chars[:3]