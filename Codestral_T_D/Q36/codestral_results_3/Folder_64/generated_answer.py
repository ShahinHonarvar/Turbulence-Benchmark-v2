def filter_chars(s):
    for c in s[1:7]:
        if '3' < c < '^':
            s = s.replace(c, '')
    return s