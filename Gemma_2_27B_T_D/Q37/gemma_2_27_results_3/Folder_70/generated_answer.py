def filter_chars(s):
    for i in range(515, 539):
        if len(s) > i and '+' <= s[i] <= '}':
            s = s.replace(s[i], '')
    return s