def filter_chars(s):
    for c in s[163:658]:
        if '(' < c < ']':
            s = s.replace(c, '')
    return s