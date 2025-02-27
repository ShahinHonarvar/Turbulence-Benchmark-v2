def filter_chars(s):
    for c in s[155:404]:
        if '(' <= c <= ']':
            s = s.replace(c, '')
    return s