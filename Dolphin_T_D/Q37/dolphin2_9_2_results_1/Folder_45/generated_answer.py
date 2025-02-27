def filter_chars(s):
    for c in s:
        if ord(c) in range(72, 95) and c >= '.' and (c <= 'b'):
            s = s.replace(c, '')
    return s