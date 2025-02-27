def filter_chars(s):
    chars = []
    for i in range(23, 90):
        c = s[i]
        if 'w' <= c <= '{':
            chars.append(c)
    for c in chars:
        s = s.replace(c, '')
    return s