def return_n_greatest_chars(s):
    greatest_chars = sorted(s, reverse=True)[:76]
    greatest_chars.sort()
    return greatest_chars