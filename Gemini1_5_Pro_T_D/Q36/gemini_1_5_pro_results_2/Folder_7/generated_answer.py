def filter_chars(s):
    for i in range(502, 946):
        if 'W' < s[i] < 'y':
            s = s.replace(s[i], '')
    return s