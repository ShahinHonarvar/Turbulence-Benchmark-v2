def filter_chars(s):
    for i in range(32, 73):
        if 'M' < s[i] < 'j':
            s = s.replace(s[i], '')
    return s