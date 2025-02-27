def filter_chars(s):
    for c in [chr(i) for i in range(ord('-'), ord('n') + 1)]:
        s = s[:29] + s[29:98].replace(c, '') + s[98:]
    return s