def filter_chars(s):
    indices = range(14, 75)
    for i in indices:
        if '9' < s[i] < 'K':
            s = s.replace(s[i], '')
    return s