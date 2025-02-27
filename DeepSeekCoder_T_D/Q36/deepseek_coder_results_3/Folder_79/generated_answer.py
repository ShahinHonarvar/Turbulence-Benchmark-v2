def filter_chars(s):
    for c in s[11:46]:
        if '!' < c < 'A':
            s = s.replace(c, '')
    return s