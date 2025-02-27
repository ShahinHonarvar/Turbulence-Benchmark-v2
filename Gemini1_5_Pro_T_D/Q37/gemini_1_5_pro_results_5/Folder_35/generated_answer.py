def filter_chars(s):
    to_remove = ''
    for i in range(155, 404):
        if i <= len(s) - 1:
            c = s[i]
            if c >= '(' and c <= ']':
                to_remove += c
    for c in to_remove:
        s = s.replace(c, '')
    return s