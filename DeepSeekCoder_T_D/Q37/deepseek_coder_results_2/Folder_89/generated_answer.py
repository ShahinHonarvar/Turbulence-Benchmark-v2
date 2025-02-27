def filter_chars(s):
    for i in range(11, 33):
        if '!' <= s[i] <= '@':
            s = s.replace(s[i], '')
    return s