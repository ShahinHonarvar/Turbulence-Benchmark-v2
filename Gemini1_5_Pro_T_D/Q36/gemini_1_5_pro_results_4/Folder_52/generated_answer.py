def filter_chars(s):
    for i in range(49, 56):
        if s[i] > 'I' and s[i] < 'a':
            c = s[i]
            s = s.replace(c, '')
    return s