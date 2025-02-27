def filter_chars(s):
    for i in range(11, 33):
        if '!' <= s[i] <= '@':
            s = s[:i] + s[i + 1:]
    return s