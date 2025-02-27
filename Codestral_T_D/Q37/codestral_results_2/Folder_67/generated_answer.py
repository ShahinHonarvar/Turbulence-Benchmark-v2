def filter_chars(s):
    for char in set(s[19:23]):
        if ']' <= char <= 't':
            s = s.replace(char, '')
    return s