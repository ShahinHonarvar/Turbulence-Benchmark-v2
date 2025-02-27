def return_n_greatest_chars(s):
    chars = [''.join(sorted(s))] * 29
    chars.sort(key=lambda x: (len(x), x), reverse=True)
    return chars[:29]