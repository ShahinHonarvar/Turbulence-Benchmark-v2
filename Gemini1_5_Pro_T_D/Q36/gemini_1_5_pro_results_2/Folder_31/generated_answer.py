def filter_chars(s):
    t = ''
    for i in range(len(s)):
        c = s[i]
        if 14 < i < 75 and '9' < c < 'K':
            t = t.replace(c, '')
        else:
            t += c
    return t