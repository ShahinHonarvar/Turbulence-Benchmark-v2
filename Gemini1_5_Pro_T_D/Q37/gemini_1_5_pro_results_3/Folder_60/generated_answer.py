def filter_chars(s):
    for i in range(12, 78):
        if i < len(s) and ':' <= s[i] <= 'L':
            c = s[i]
            s = s.replace(c, '')
    return s