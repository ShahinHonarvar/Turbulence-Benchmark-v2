def return_n_greatest_chars(s):
    chars = sorted(s, key=lambda x: x, reverse=True)
    return chars[:87]