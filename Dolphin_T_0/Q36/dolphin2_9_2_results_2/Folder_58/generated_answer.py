def filter_chars(s):
    for i in range(318, 337):
        if 'B' < s[i] < 'z':
            s = ''.join([c for c in s if c != s[i]])
    return s