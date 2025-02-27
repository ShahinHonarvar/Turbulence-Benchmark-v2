def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda x: -ord(x))
    return sorted(sorted_chars[:31])