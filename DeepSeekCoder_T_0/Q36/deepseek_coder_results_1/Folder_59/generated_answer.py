def filter_chars(s):
    for i in range(4, 8):
        if '?' < s[i] < 'k':
            s = s.replace(s[i], '')
    return s