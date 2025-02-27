def filter_chars(s):
    for char in sorted(set(s[19:23])):
        if ']' <= char <= 't':
            s = s.replace(char, '')
    return s