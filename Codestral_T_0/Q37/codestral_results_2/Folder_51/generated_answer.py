def filter_chars(s):
    for c in s[36:41]:
        if 'H' <= c <= 'e':
            s = s.replace(c, '')
    return s