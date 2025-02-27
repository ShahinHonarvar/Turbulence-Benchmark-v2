def filter_chars(s):
    for c in s[24:83]:
        if '5' <= c <= '<':
            s = s.replace(c, '')
    return s