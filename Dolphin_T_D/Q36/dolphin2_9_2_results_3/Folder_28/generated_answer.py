def filter_chars(s):
    for c in range(31, 73):
        if 'M' < s[c] < 'j':
            s = s.replace(s[c], '')
    return s