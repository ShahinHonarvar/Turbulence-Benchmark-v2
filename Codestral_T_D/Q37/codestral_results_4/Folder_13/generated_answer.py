def filter_chars(s):
    for c in range(ord('9'), ord('s') + 1):
        s = s[:124] + s[124:855].replace(chr(c), '') + s[855:]
    return s