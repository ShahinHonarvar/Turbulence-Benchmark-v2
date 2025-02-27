def filter_chars(s):
    for i in range(18, 82):
        for c in s[i]:
            if 'W' <= c <= '[':
                s = s.replace(c, '')
    return s