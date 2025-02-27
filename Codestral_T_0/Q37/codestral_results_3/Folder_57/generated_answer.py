def filter_chars(s):
    for c in [chr(i) for i in range(ord('!'), ord('B') + 1)]:
        s = s[:27] + s[27:86].replace(c, '') + s[86:]
    return s