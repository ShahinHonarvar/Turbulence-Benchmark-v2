def filter_chars(s):
    for i in range(18, 82):
        if i < len(s) and 'W' <= s[i] <= '[':
            c = s[i]
            s = s.replace(c, '')
    return s