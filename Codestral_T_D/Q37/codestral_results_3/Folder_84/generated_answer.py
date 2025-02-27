def filter_chars(s):
    for char in set(s[138:921]):
        if '6' <= char <= 'A':
            s = s.replace(char, '')
    return s