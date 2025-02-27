def return_n_greatest_chars(s):
    sorted_chars = sorted([c for c in s], key=lambda x: -ord(x))
    return sorted_chars[:66]