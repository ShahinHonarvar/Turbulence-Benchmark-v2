def filter_chars(s):
    for i in range(421, 854):
        c = s[i]
        if 'D' < c < 'J':
            s = s[:i] + s[i + 1:]
    return s