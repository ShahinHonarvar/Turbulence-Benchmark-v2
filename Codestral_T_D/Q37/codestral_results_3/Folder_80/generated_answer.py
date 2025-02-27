def filter_chars(s):
    for char in sorted(set(s[36:80])):
        if 'a' <= char <= 'i':
            s = s.replace(char, '')
    return s