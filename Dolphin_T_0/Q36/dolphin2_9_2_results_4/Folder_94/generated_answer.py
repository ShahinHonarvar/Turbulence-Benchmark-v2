def filter_chars(s):
    for c in range(15, 85):
        if 'I' < s[c] < 'M':
            s = s.replace(s[c], '')
    return s