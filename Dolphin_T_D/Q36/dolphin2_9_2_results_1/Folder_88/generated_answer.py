def filter_chars(s):
    for i in range(78, 81):
        for c in s:
            if c > 'S' and c < '[':
                s = s.replace(c, '')
    return s