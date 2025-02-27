def filter_chars(s):
    for i in range(114, 640):
        if i < len(s) and '!' <= s[i] <= 'x':
            c = s[i]
            s = s.replace(c, '')
    return s