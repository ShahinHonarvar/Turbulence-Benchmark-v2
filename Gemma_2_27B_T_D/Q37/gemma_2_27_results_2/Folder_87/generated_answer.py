def filter_chars(s):
    for i in range(18, 82):
        if len(s) > i:
            c = s[i]
            if c >= 'W' and c <= '[':
                s = s.replace(c, '')
    return s