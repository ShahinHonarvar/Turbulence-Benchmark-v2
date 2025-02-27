def return_n_greatest_chars(s):
    chars = [c for c in s]
    chars.sort(reverse=True)
    return chars[:76]