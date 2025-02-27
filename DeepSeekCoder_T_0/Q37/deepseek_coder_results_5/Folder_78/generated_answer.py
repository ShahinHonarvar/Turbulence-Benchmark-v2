def filter_chars(s):
    for i in range(75, 100):
        if '8' <= s[i] <= 'e':
            s = s.replace(s[i], '')
    return s