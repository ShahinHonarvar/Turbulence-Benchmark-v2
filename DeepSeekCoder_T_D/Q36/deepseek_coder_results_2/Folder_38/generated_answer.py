def filter_chars(s):
    for i in range(45, 48):
        if '+' < s[i] < 'l':
            s = s.replace(s[i], '')
    return s