def filter_chars(s):
    for i in range(49, 56):
        if s[i] > 'I' and s[i] < 'a':
            s = s.replace(s[i], '')
    return s