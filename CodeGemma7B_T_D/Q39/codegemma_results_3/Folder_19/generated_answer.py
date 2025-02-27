def return_n_greatest_chars(s):
    while len(s) != 58:
        s += chr(ord(s[-1]) - 1)
    s = sorted(s, key=ord)
    return s