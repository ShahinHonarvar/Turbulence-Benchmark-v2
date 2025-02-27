def filter_chars(s):
    for c in range(ord('c'), ord('i') + 1):
        s = s[:27] + s[27:86].replace(chr(c), '') + s[86:]
    return s