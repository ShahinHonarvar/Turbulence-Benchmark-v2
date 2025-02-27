def filter_chars(s):
    for char in set(s[155:404]):
        if '(' <= char <= ']':
            s = s.replace(char, '')
    return s