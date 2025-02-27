def filter_chars(s):
    for c in range(42, 68):
        if 't' < s[c] < 'x':
            s = s.replace(s[c], '')
    return s