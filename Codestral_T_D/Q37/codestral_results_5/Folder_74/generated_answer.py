def filter_chars(s):
    for c in [chr(i) for i in range(ord('f'), ord('o') + 1)]:
        s = s[:19] + s[19:33].replace(c, '') + s[33:]
    return s