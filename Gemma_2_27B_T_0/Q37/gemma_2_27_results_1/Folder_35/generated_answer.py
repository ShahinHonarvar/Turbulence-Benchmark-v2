def filter_chars(s):
    for i in range(155, 404):
        if s[i] >= '(' and s[i] <= ']':
            s = s.replace(s[i], '')
    return s