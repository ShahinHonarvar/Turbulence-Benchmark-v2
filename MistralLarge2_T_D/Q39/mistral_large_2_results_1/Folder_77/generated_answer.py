def return_n_greatest_chars(s):
    sorted_chars = sorted(s)[-47:]
    sorted_chars.sort()
    return sorted_chars