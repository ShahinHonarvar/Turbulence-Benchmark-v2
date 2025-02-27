def filter_chars(s):
    r = ''
    for c in s:
        d = ord(c)
        if not (71 <= d <= 94 and 75 <= d <= 97):
            r += c
    return r