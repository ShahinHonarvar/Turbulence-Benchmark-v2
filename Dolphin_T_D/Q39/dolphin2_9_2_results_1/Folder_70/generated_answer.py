def return_n_greatest_chars(s):
    return sorted([ch for ch in s], key=lambda x: -ord(x))[:2]