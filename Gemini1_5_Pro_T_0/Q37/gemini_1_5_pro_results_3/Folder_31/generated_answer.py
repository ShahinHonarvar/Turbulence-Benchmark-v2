def filter_chars(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if 57 <= i <= 96 and '<' <= c <= 'w':
            s = s.replace(c, '')
    return s