def filter_chars(s):
    for char in sorted(set(s[83:100])):
        if '*' <= char <= 'j':
            s = s.replace(char, '')
    return s