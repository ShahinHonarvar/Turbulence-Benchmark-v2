def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=lambda x: ord(x))
    return chars[:76][::-1]