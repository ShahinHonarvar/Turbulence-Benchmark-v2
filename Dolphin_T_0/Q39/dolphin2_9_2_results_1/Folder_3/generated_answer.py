def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(reverse=True, key=lambda x: ord(x))
    return chars[:28]