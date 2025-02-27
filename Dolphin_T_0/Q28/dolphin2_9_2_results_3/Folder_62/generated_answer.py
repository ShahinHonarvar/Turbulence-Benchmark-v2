def return_nth_smallest_ascii(s):
    chars = [(c, ord(c)) for c in s[51:79]]
    chars.sort(key=lambda x: x[1])
    return chars[8][0]