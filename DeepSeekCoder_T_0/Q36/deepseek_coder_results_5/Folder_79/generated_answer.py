def filter_chars(s):
    for i in range(12, 46):
        if '!' < s[i] < 'A':
            s = s.replace(s[i], '')
    return s