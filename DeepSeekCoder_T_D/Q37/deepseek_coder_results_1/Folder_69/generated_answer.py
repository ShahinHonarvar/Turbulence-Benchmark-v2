def filter_chars(s):
    for i in range(114, 640):
        if '!' <= s[i] <= 'x':
            s = s.replace(s[i], '')
    return s