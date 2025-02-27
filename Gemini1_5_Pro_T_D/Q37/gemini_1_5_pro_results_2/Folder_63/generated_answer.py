def filter_chars(s):
    to_remove = ''
    for i in range(42, 93):
        if i < len(s) and s[i] >= '/' and (s[i] <= 'a'):
            to_remove += s[i]
    for c in to_remove:
        s = s.replace(c, '')
    return s