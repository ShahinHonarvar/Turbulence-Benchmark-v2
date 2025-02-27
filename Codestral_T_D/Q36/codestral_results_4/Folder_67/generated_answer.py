def filter_chars(s):
    for c in s[18:31]:
        if 'H' < c < '|':
            s = s.replace(c, '')
    return s