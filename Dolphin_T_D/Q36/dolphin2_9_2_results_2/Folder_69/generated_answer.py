def filter_chars(s):
    for i in range(343, 665):
        if s[i] > '%' and s[i] < 'U':
            s = ''.join((c for c in s if c != s[i]))
    return s