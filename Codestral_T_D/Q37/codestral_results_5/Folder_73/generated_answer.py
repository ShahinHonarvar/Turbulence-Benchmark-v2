def filter_chars(s):
    for char in set(s[22:86]):
        if '7' <= char <= 'e':
            s = s.replace(char, '')
    return s