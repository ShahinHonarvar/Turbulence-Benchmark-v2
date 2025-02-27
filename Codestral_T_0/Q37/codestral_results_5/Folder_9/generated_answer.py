def filter_chars(s):
    for c in [chr(i) for i in range(ord('A'), ord('Q') + 1)]:
        s = s[:38] + s[38:99 + 1].replace(c, '') + s[99 + 1:]
    return s