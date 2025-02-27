def filter_chars(s):
    for c in [chr(i) for i in range(ord('H'), ord('s') + 1)]:
        s = s[:35] + s[35:52].replace(c, '') + s[52:]
    return s