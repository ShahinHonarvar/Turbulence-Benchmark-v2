def filter_chars(s):
    for i in range(2):
        for c in s:
            if '*' <= c <= 's' and c in s:
                s = s.replace(c, '')
    return s