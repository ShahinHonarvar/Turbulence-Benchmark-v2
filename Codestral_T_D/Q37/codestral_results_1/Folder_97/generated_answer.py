def filter_chars(s):
    for char in s[227:236]:
        if 'D' <= char <= 'u':
            s = s.replace(char, '')
    return s