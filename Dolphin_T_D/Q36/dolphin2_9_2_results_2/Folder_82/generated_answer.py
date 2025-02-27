def filter_chars(s):
    for i in range(69, 97):
        if s[i] > 'V' and s[i] < 'j':
            s = s.replace(s[i], '')
    return s