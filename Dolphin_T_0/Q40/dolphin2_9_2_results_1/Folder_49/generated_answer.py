def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort()
    return chars[:76][::-1]