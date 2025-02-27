def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda x: -ord(x))[:38]
    return sorted(sorted_chars)