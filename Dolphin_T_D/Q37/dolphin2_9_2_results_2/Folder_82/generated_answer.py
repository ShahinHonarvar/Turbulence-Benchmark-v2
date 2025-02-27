def filter_chars(s):
    for i in range(12, 26):
        c = s[i]
        if 'P' <= c <= 'x':
            s = s[:i] + s[i:].replace(c, '')
    return s