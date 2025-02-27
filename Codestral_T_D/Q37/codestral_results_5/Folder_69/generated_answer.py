def filter_chars(s):
    for c in sorted(set(s[114:640])):
        if '!' <= c <= 'x':
            s = s.replace(c, '')
    return s