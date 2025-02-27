def filter_chars(s):
    for c in [chr(i) for i in range(ord('7'), ord('k') + 1)]:
        s = s[:33] + s[33:71].replace(c, '') + s[71:]
    return s