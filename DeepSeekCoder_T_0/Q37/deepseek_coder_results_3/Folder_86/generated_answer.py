def filter_chars(s):
    for i in range(164, 707):
        if 'O' <= s[i] <= '}':
            s = s.replace(s[i], '')
    return s