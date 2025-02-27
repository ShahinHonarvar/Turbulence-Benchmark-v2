def filter_chars(s):
    for i in range(33, 71):
        if '7' <= s[i] <= 'k':
            s = s.replace(s[i], '')
    return s