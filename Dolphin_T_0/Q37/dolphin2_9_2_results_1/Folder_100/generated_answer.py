def filter_chars(s):
    for c in s:
        if 88 <= ord(c) <= 90 and 'J' <= c <= 'Q':
            s = s.replace(c, '')
    return s