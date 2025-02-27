def filter_chars(s):
    for i in range(515, 539):
        if i < len(s):
            c = s[i]
            if '+' <= c <= '}':
                s = s.replace(c, '')
    return s