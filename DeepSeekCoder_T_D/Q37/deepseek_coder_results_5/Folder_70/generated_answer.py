def filter_chars(s):
    for i in range(515, 539):
        if '+' <= s[i] <= '}':
            s = s.replace(s[i], '')
    return s