def filter_chars(s):
    for c in [chr(i) for i in range(ord('2'), ord('s') + 1)]:
        s = s[:36] + s[36:80].replace(c, '') + s[80:]
    return s