def filter_chars(s):
    for c in [chr(i) for i in range(ord(':'), ord('L') + 1)]:
        s = s[:12] + s[12:78].replace(c, '') + s[78:]
    return s