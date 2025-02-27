def filter_chars(s):
    for c in s[18:38]:
        if ')' < c < 'P':
            s = s.replace(c, '')
    return s