def filter_chars(s):
    for c in s:
        if 32 <= ord(c) <= 61 and '3' < c < 'D':
            s = s.replace(c, '')
    return s