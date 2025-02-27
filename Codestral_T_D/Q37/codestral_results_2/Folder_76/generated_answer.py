def filter_chars(s):
    for c in [chr(i) for i in range(ord('M'), ord('v') + 1)]:
        s = s[:379] + s[379:899].replace(c, '') + s[899:]
    return s