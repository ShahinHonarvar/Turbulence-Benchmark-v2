def filter_chars(s):
    for c in s[78:81]:
        if 'S' < c < '[':
            s = s.replace(c, '')
    return s