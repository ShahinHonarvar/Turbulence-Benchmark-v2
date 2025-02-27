def filter_chars(s):
    for i in range(23, 83):
        if s[i] > 'f' and s[i] < 'o':
            s = ''.join([c for c in s if c != s[i]])
    return s