def filter_chars(s):
    for i in range(32, 47):
        if '0' <= s[i] <= 'k':
            s = s.replace(s[i], '')
    return s