def filter_chars(s):
    for i in range(32, 50):
        if '/' < s[i] < 'J':
            s = s.replace(s[i], '')
    return s