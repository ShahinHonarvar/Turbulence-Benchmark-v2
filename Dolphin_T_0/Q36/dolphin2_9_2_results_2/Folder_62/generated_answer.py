def filter_chars(s):
    indices = range(63, 89)
    for i in indices:
        if '*' < s[i] < 'w':
            s = s.replace(s[i], '')
    return s