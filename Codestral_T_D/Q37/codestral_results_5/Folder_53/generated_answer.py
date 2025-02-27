def filter_chars(s):
    for c in [chr(i) for i in range(ord('*'), ord('j') + 1)]:
        s = s[:83] + s[83:100].replace(c, '') + s[100:]
    return s