def filter_chars(s):
    for c in [chr(i) for i in range(ord('f'), ord('|') + 1)]:
        s = s[:41] + s[41:80].replace(c, '') + s[80:]
    return s