def filter_chars(s):
    for i in range(26, min(65, len(s))):
        if 'V' <= s[i] <= 'o':
            s = s.replace(s[i], '')
    return s