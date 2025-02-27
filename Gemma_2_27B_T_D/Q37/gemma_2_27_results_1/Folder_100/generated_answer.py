def filter_chars(s):
    for i in range(88, 91):
        for c in s:
            if ord(c) == i and c >= 'J' and (c <= 'Q'):
                s = s.replace(c, '')
    return s