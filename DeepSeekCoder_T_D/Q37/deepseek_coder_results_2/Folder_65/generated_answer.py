def filter_chars(s):
    for i in range(61, 71):
        if '0' <= s[i] <= '@':
            s = s.replace(s[i], '')
    return s