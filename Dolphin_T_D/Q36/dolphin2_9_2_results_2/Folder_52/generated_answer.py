def filter_chars(s):
    for i in range(49, 56):
        if 'I' < s[i] < 'a':
            s = s.replace(s[i], '')
    return s