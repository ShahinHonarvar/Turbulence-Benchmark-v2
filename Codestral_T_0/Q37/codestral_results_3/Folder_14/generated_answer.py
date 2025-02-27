def filter_chars(s):
    for c in [chr(i) for i in range(ord('A'), ord('b') + 1)]:
        s = s[:35] + s[35:99].replace(c, '') + s[99:]
    return s