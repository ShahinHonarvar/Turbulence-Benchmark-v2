def return_n_greatest_chars(s):
    sorted_chars = sorted([c for c in s], key=lambda x: -ord(x))[:27]
    return sorted_chars